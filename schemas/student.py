

def studentEntity(db_item)->dict:
    return{
        "id":str(db_item["_id"]),
        "student_name":db_item["student_name"],
        "email":db_item["student_email"],
        "phone":db_item["student_phone"]
    }
def list_student_Entity(db_item_list)->list:
    list_stud_ent=[]
    for item in db_item_list:
        list_stud_ent.append(studentEntity(item))
    return list_stud_ent