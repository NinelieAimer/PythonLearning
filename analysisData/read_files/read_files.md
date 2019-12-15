# 文件读取

> ​	因为我们解除的数据类型不多，所以先试着列一下

| 函数         | 描述                     |
| ------------ | ------------------------ |
| read_csv     | 读取csv，按照逗号分隔的  |
| read_table   | 读取表格，按照制表符分割 |
| read_excel   | 读取xls或者xlsx文件      |
| read_html    | 读取html中所有表格       |
| read_json    | 读取json文件             |
| read_sql     | 读取SQL查询结果          |
| read_stata   | 读取stata格式数据文件    |
| read_sas     | 读取sas格式文件          |
| read_feather | 读取二进制格式           |

## 一些参数和方法

- **header=None这个参数可以让数据没有头部，一般的数据都会有列属性，当你不需要的时候，就可以使用None**

  ```python
  df=pd.read_csv('E:\\learning\\spssModelerLearning\\tantannic\\titanic_train .csv',header=None)
  #这样就会没有表头，
  ```

- 还可以换==头部==，在读取的时候，使用names参数就可以

  ```python
  df=pd.read_csv('test.csv',names=['time','name','slim'])
  ```

- python的默认索引是0，1，2，如果你想用某一列作为索引就可以使用index_col参数

  ```python
  df=pd.read_csv('E:\\learning\\spssModelerLearning\\tantannic\\titanic_train .csv',index_col='PassengerId')
  #这里我们就使用PassengerId作为行索引
  ```

- ==注意：如果列名数量比数据的列少了一个，会把这一列作为当前行索引用的==

- 使用skiprows可以跳过特定的行

  ```python
  df=pd.read_csv('test.csv',skiprows=[0,2,3])
  #这里我们选择跳过1，3，4行
  ```

- 对于NULL和NaN的数字，我们可以用isnull来判断，然后会生成一个布尔值列表

**一些常用的参数：**

| 参数               | 描述                                                         |
| ------------------ | ------------------------------------------------------------ |
| filepath_or_buffer | 文件路径                                                     |
| sep                | 分隔符                                                       |
| header             | 默认是0，就是第一行，没有就要传入None                        |
| skiprows           | 需要跳过的行号，或者行号==列表==                             |
| na_values          | 需要用NA替换的值序列                                         |
| comment            | 在行结尾处分隔注释的字符                                     |
| parse_dates        | 尝试将数据解析为datetime，默认为False                        |
| converters         | 传入字典格式，Key为列，可以传入函数（例如{'test':f},这个就是将f函数传递到test行上） |
| nrows              | 这个写入读入的行数                                           |
| skip_footer        | 忽略文件尾部的行数                                           |
| encoding           | 文件编码，如果有中文，建议使用'gbk'                          |

- 如果要将文件保存到excel格式，就要使用to_excel方法

  ```
  frame.to_excel('fjlaskjfljak/dfa.xlsx')
  ```


## 关于Excel写入操作

- 如果写入时候不想把DataFrame中的索引带进来，使用`index=False`**就可以取消前面索引**

- 如果你想把多个表写到同一个excel中，只是分**sheet**，可以如下操作

  - ```python
    writer=pd.WriterExcel('test.xlsx')	#初始化一个写Excel对象
    
    #将两个不同的DataFrame存入同一个Excel的不同sheet
    temp1.to_excel(writer,sheet_name='data1',index=False)
    temp2.to_excel(writer,sheet_name='data2',index=False)
    ```

## 关于PDF的读写

> ​	很多时候我们要将PDF的东西读取出来，这个时候就需要用pdfminer3了，具体源码如下

```python
from pdfminer3.layout import LAParams, LTTextBox
from pdfminer3.pdfpage import PDFPage
from pdfminer3.pdfinterp import PDFResourceManager
from pdfminer3.pdfinterp import PDFPageInterpreter
from pdfminer3.converter import PDFPageAggregator
from pdfminer3.converter import TextConverter
import io

resource_manager = PDFResourceManager()
fake_file_handle = io.StringIO()
converter = TextConverter(resource_manager, fake_file_handle)
page_interpreter = PDFPageInterpreter(resource_manager, converter)

with open('./Python_Learning.pdf', 'rb') as fh:	#一定要用rb模式

    for page in PDFPage.get_pages(fh,
                                  caching=True,
                                  check_extractable=True):
        page_interpreter.process_page(page)

    pdf_text = fake_file_handle.getvalue()
converter.close()
fake_file_handle.close()
```



## PDF中表格提取

> ​	很多情况下，我们需要将PDF中的表格提取出来，这时候就需要**tabula-py**这个包，**注意**：这个包需要装Java环境，所以需要下Java，具体可访问网站[tutorial]( https://aegis4048.github.io/parse-pdf-files-while-retaining-structure-with-tabula-py )，查看，里面有很多东西

```python
import tabula


#这里很多东西
df=tabula.read_pdf(input_path='./2016-year_report.pdf',
pages='all',lattice=True,	
pandas_options={'header':None},multiple_tables=True)
```

- `pages`：这个作用是选择需要搜索的页面，all代表，搜索所有页面
- `lattice`：这个对于搜索网格线组成表有重要意义
- `multiple_table`：这个非常重要，这个为`True`说明里面有多个不同表格，会返回一个列表，列表中每一个是一个DataFrame对象
- `pandas_options`：这个东西用在是传入在创建表格时候一些选项，比如header要不要，列名要不要换如果还需要，自己去看文档吧



