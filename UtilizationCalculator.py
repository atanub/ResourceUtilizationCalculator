import logging
import traceback
import datetime
import json
import pandas as pd
from dateutil.relativedelta import relativedelta


class UtilizationCalculator():
    """
    A utility class for calculating utilization based on input data.
    input data consists of allocations across multiple projects with varying durations and timeframes.
    Methods
    -------
    calculate(inputFilePath, outputFilePath, countOfPastMonths, countOfFutureMonths, autoDetectTenure=False)
        Main method to calculate utilization and save the result to a file.
    """

    @staticmethod
    def calculate(inputFilePath, outputFilePath, countOfPastMonths, countOfFutureMonths, autoDetectTenure=False):
        df = UtilizationCalculator._readInputFile(inputFilePath)
        if autoDetectTenure is True:
            maxDate = df.EndDate.max()
            minDate = df.StartDate.min()
            minDate = datetime.date(minDate.year, minDate.month, 1)
            lastMonth = minDate - datetime.timedelta(days=1)
            minDate = datetime.date(lastMonth.year, lastMonth.month, 1)
            tmpDate = maxDate + relativedelta(months=+1)
            maxDate = datetime.date(tmpDate.year, tmpDate.month, 1)
        else:
            minDate = datetime.datetime.now() + relativedelta(months=+(-countOfPastMonths-1))
            minDate = datetime.date(minDate.year, minDate.month, 1)
            # //
            maxDate = datetime.datetime.now() + relativedelta(months=+
                                                              (countOfFutureMonths+1))
            maxDate = datetime.date(maxDate.year, maxDate.month, 1)
            maxDate = maxDate - datetime.timedelta(days=1)

        # 7D = A week; M = Month
        dateRanges = pd.date_range(start=minDate,
                                   end=maxDate, freq='M')

        logging.debug(
            f"Overall Date Range for considering allocation data: {minDate} - {maxDate}")
        logging.debug('-' * 16)
        result = UtilizationCalculator._calcUtilization(
            df, dateRanges)
        outputFile = outputFilePath
        UtilizationCalculator._saveInDisk(result, outputFile)
        logging.debug('-' * 16)
        pass

    @staticmethod
    def _readInputFile(inputFile):
        df = pd.read_csv(inputFile, delimiter='\t', encoding='utf-8')
        df = df.filter(['Name', 'StartDate', 'EndDate', 'Allocation'])
        # //
        df['StartDate'] = pd.to_datetime(df['StartDate'])
        df['EndDate'] = pd.to_datetime(df['EndDate'])
        df['interval'] = df['EndDate'] - df['StartDate']

        # logging.debug(df.dtypes)
        # logging.debug(list(df.columns.values)) #file header
        # logging.debug(df.tail(10)) #last 10 rows
        # Filter out records of future dates
        # df = df[df['EndDate'] > pd.Timestamp(datetime.datetime.now())]
        df = df.sort_values('StartDate')
        # logging.debug(df.tail(1000)) #last N rows
        return df

    @staticmethod
    def _calcUtilizationEx(df, startDate, endDate):
        d = startDate
        count = 0
        uu = 0
        while d <= endDate:
            u = UtilizationCalculator._calcUtilizationForOneDay(df, d)
            uu += u
            count += 1
            d += datetime.timedelta(days=1)

        uu = uu / count
        return uu

    @staticmethod
    def _calcUtilizationForOneDay(df, dateToCalcUtil):
        dateToCalcUtil = pd.Timestamp(dateToCalcUtil)
        match = df.loc[(dateToCalcUtil >= df['StartDate'])
                       & (dateToCalcUtil <= df['EndDate'])]
        if match.size == 0:
            return 0.0

        u = match["Allocation"].sum()
        return u

    @staticmethod
    def _calcUtilization(df, dateRanges):
        result = []
        dfByName = df.groupby("Name")
        for name, dfTemp in dfByName:
            logging.debug(f"Allocation Input for {name!r}")
            logging.debug(dfTemp.head(100))

            di = {
                "Name": name,
            }
            o = UtilizationCalculator._calcUtilizationForAnEmployee(
                name, dfTemp, dateRanges)
            di['utilization'] = o
            #
            result.append(di)

        return result

    @staticmethod
    def _calcUtilizationForAnEmployee(name, df, dateRanges):
        startDate = None
        logging.debug(f"Calculating Utilization of '{name}':")
        o = []
        for endDt in dateRanges:
            endDt = endDt.date()
            if startDate is None:
                startDate = endDt
                continue

            u = UtilizationCalculator._calcUtilizationEx(
                df, startDate, endDt)
            logging.debug(f"{startDate} - {endDt}: {round(u*100,2)}%")

            # dtRange = f'{startDate.strftime("%Y-%m-%d")} - {endDt.strftime("%Y-%m-%d")}'
            oo = {
                'start': startDate.strftime("%Y-%m-%d"),
                'end': endDt.strftime("%Y-%m-%d"),
                'utilization': u
            }
            o.append(oo)
            startDate = endDt + datetime.timedelta(days=1)

        return o

    @staticmethod
    def _saveInDisk(result, outputFile):
        # s = json.dumps(result)
        with open(outputFile, 'w', encoding="utf-8") as f:
            json.dump(result, f)
            logging.info(f"File: {outputFile} saved successfully")
            pass
        pass


if __name__ == "__main__":
    logLevel = "DEBUG"
    logging.getLogger().setLevel(logLevel)

    try:
        inputFilePath = 'output/Sample Input - Utilization Calculator.tsv'
        outputFilePath = 'output/Utilization Calculator Output.json'
        countOfPastMonths = 4
        countOfFutureMonths = 4
        UtilizationCalculator.calculate(
            inputFilePath, outputFilePath, countOfPastMonths, countOfFutureMonths)

    except Exception as error:
        logging.error(f'Job execution failed! Error: {error}.')
        logging.error('>!<' * 24)
        traceback.print_exc()
        logging.error('>!<' * 24)
