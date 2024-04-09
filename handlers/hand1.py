def test(hashMap,_files=None,_data=None):
  if hashMap.get("listener") == "btn2":
      hashMap.put("toast", "123")

  return hashMap

def init_on_start(hashMap,_files=None,_data=None):

   hashMap.put("SQLConnectDatabase","test1.DB")
   hashMap.put("SQLExec",json.dumps({"query":"create table IF NOT EXISTS Record(id integer primary key autoincrement,art text, barcode text, name text, qty real)","params":""}))

   return hashMap