# TeamUtilizationCalculator
Calculates team members' utilization based on their allocations across multiple projects with varying durations and timeframes.

# Check Sample Data files
* [Sample Input](./Sample%20Data/Sample%20Input%20-%20Utilization%20Calculator.tsv)
* [Output](./Sample%20Data/Sample%20Output%20-%20Utilization%20Calculator.json)


# Illustration

System calculates utilization for each day to calculate average utilization for a month. This logic needs to be revamped by avoidong day wise calculation!

* Input
Refer to the below sample input data listing only the key fields required for the utilization calculation

```tsv
Name	StartDate	EndDate	ProjectName	Allocation
Bob	19-Mar-2025	25-Jun-2025	Gamma	0.50
Bob	28-Apr-2025	20-Jun-2025	Gamma	0.75
Bob	11-Apr-2025	23-Jun-2025	Omega	0.25
Diana	20-Feb-2025	04-Jun-2025	Alpha	0.25
Diana	08-Feb-2025	22-Jun-2025	Omega	0.25
Diana	06-Mar-2025	29-May-2025	Beta	0.75
Ethan	15-Feb-2025	16-Apr-2025	Omega	0.50
Charlie	04-Feb-2025	02-Mar-2025	Delta	0.50
Charlie	03-Apr-2025	17-Apr-2025	Gamma	0.50
Charlie	02-Mar-2025	26-May-2025	Alpha	0.75
```

* Output
Result of Utilization calculation for Bob

```json
[
    {
        "Name": "Bob",
        "utilization": [
            {
                "start": "2024-08-31",
                "end": "2024-09-30",
                "utilization": 0.0
            },
            {
                "start": "2024-10-01",
                "end": "2024-10-31",
                "utilization": 0.0
            },
            {
                "start": "2024-11-01",
                "end": "2024-11-30",
                "utilization": 0.0
            },
            {
                "start": "2024-12-01",
                "end": "2024-12-31",
                "utilization": 0.0
            },
            {
                "start": "2025-01-01",
                "end": "2025-01-31",
                "utilization": 0.0
            },
            {
                "start": "2025-02-01",
                "end": "2025-02-28",
                "utilization": 0.0
            },
            {
                "start": "2025-03-01",
                "end": "2025-03-31",
                "utilization": 0.20967741935483872
            },
            {
                "start": "2025-04-01",
                "end": "2025-04-30",
                "utilization": 0.7416666666666667
            },
            {
                "start": "2025-05-01",
                "end": "2025-05-31",
                "utilization": 1.5
            }
        ]
    }
]
```
