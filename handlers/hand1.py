def test(hashMap,_files=None,_data=None):
	if hashMap.get("listener") == "btn2":
			hashMap.put("toast", "123")

	return hashMap

def init_on_start(hashMap,_files=None,_data=None):

	hashMap.put("SQLConnectDatabase","test1.DB")
	hashMap.put("SQLExec",json.dumps({"query":"create table IF NOT EXISTS Record(id integer primary key autoincrement,art text, barcode text, name text, qty real)","params":""}))

	return hashMap

def input_qty(hashMap,_files=None,_data=None):
	from ru.travelfood.simple_ui import SimpleSQLProvider as sqlClass
	sql = sqlClass()
	success=sql.SQLExec("insert into Record(barcode,name,qty) values(?,?,?)",hashMap.get('bcode')+","+hashMap.get("text_product")+","+str(hashMap.get("qty")))
	success = True

	if success:
					hashMap.put("ShowScreen","Сканирование")
					hashMap.put("toast","Добавлено" + hashMap.get("text_product"))


	return hashMap

def on_start_barcode(hashMap,_files=None,_data=None):

		rows=[]

		table  = {
		"type": "table",
		"textsize": "20",

		"columns": [
		{
				"name": "barcode",
				"header": "[Barcode]",
				"weight": "2"
		},
		{
				"name": "name",
				"header": "Name",
				"weight": "2"
		},
			{
				"name": "qty",
				"header": "[Qty]",
				"weight": "1"
		}
		]
		}

		sql = sqlClass()
		res = sql.SQLQuery("select * from Record","")

		records = json.loads(res)
		for record in records:
		    rows.append({"barcode":record['barcode'],"name":record['name'],"qty":str(record['qty'])})

		table['rows'] =rows
		hashMap.put("table",json.dumps(table))

		return hashMap

def on_start_barcode1(hashMap,_files=None,_data=None):

		table  = {
		"type": "table",
		"textsize": "25",
		"hidecaption": "true",
		"hideinterline": "true",
		"columns": [
			{
				"name": "nom",
				"header": "Товар",
				"weight": "2"
			},
			{
				"name": "qty",
				"header": "Кол-во",
				"weight": "1"
			},
			{
				"name": "price",
				"header": "Цена",
				"weight": "1"
			}
		],
		"rows": [
			{
				"nom": "Процессов Intel Core 9 OEM",
				"qty": "5",
				"price": "15500.00"
			},
			{
				"nom": "Процессов Intel Core 5 BOX",
				"qty": "-2",
				"price": "12500.00"
			},
			{
				"nom": "Процессов Intel Core 5 (OEM)",
				"qty": "2",
				"price": "11500.00"
			}
		],
		"colorcells": [
			{
				"row": "1",
				"column": "1",
				"color": "#d81b60"
			}
		]
		}

		# sql = sqlClass()
		# res = sql.SQLQuery("select * from Record","")

		# records = json.loads(res)
		# for record in records:
		#     rows.append({"barcode":record['barcode'],"name":record['name'],"qty":str(record['qty'])})

		# table['rows'] =rows
		# hashMap.put("table",json.dumps(table))

		return hashMap