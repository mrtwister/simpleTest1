def test(hashMap,_files=None,_data=None):
  if hashMap.get("listener") == "btn2":
      hashMap.put("toast", "123")

  return hashMap

def init_on_start(hashMap,_files=None,_data=None):

   hashMap.put("SQLConnectDatabase","test1.DB")
   hashMap.put("SQLExec",json.dumps({"query":"create table IF NOT EXISTS Record(id integer primary key autoincrement,art text, barcode text, name text, qty real)","params":""}))

   return hashMap

def input_qty(hashMap,_files=None,_data=None):

   #sql = sqlClass()
   #success=sql.SQLExec("insert into Record(barcode,name,qty) values(?,?,?)",hashMap.get('bcode')+","+hashMap.get("text_product")+","+str(hashMap.get("qty")))
   success = True

   if success:
           hashMap.put("ShowScreen","Сканирование")
           hashMap.put("toast","Добавлено" + hashMap.get("text_product"))


   return hashMap