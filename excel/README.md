
## openpyxl
```python
import openpyxl
```
* load_workbook(filename, data_only=True or False)
  * get_sheet_name()
  * create_sheet(index=n, title='name')
  * get_sheet_names()
  * remove_sheet(Worksheet)
* save(filename) 

## Font
```python
from openpyxl.styles import Font

font_obj = Font(name='Times New Roman', size=24, bold=True, italic=True)

sheet['A1'].font = font_obj
```

## Chart
```python
import openpyxl

ref_obj = openpyxl.chart.Reference(data_sheet, min_col=1, min_row=1, max_col=1, max_row=10)
openpyxl.Workbook().active.add_chart(
    openpyxl.chart.BarChart().append(
        openpyxl.chart.Series(
            openpyxl.chart.Reference(
                ref_sheet, title='title'
            )
        )
    )
)

```
