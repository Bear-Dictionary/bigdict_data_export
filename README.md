# Bigdict data export

Use this tool for export data from Bigdict server. You need have an access to Mongo server. The script was created with
Python 3.

### How to use

```bash
python3 main.py <Dictionary name> --output <Output file> --address mongodb://username:password@localhost:27017
```

Result will be a csv file with following contents:

```csv
"tấm","VIE","RUS","<br>&nbsp;<font color=""goldenrod"">►</font> штука, плитка, плита, планка, пластинка, крупа, лист, лопасть, листовой"
"tấm biển","VIE","RUS","<br>&nbsp;<font color=""goldenrod"">►</font> вывеска"
"tấm gương","VIE","RUS","<br>&nbsp;<font color=""goldenrod"">►</font> пример"
```