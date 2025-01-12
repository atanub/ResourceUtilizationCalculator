# TeamUtilizationCalculator
Calculates team members' utilization based on their allocations across multiple projects with varying durations and timeframes.

# Check Sample Data files
* [Sample Input](./Sample%20Data/Sample%20Input%20-%20Utilization%20Calculator.tsv)
* [Output](./Sample%20Data/Sample%20Output%20-%20Utilization%20Calculator.json)


# Illustration

* Input
Refer to the below sample input data listing only the key fields required for the utilization calculation

```tsv
Name	StartDate	EndDate	ProjectName	Allocation
Bob	19-Mar-2025	25-Jun-2025	Project Gamma	50
Bob	28-Apr-2025	20-Jun-2025	Project Gamma	75
Bob	11-Apr-2025	23-Jun-2025	Project Omega	25
Charlie	04-Feb-2025	02-Mar-2025	Project Delta	50
Charlie	03-Apr-2025	17-Apr-2025	Project Gamma	50
Charlie	02-Mar-2025	26-May-2025	Project Alpha	75
Diana	20-Feb-2025	04-Jun-2025	Project Alpha	25
Diana	08-Feb-2025	22-Jun-2025	Project Omega	25
Diana	06-Mar-2025	29-May-2025	Project Beta	75
Ethan	15-Feb-2025	16-Apr-2025	Project Omega	50
```

* Output [WORNG - NEEDS FIX]
Result of Utilization calculation for Bob

```json
[
    {
        "Name": "Bob",
        "utilization": [
            
            {
                "start": "2025-03-01",
                "end": "2025-03-31",
                "utilization": 1.6685893400736822
            },
            {
                "start": "2025-04-01",
                "end": "2025-04-30",
                "utilization": 5.178690027711945
            },
            {
                "start": "2025-05-01",
                "end": "2025-05-31",
                "utilization": 5.005768020221047
            }
        ]
    }
]
```
