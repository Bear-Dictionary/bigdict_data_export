# Bigdict data export

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