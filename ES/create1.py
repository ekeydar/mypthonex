import json
def create_employee(first_name,last_name,age,about,interests):
    assert isinstance(first_name,basestring)
    assert isinstance(last_name,basestring)
    assert isinstance(about,basestring)
    assert isinstance(interests,list)
    assert isinstance(age,int)
    return dict(first_name=first_name,
                last_name=last_name,
                age=age,
                about=about,
                interests=interests)

def add_employee(did,emp):
    import requests
    r = requests.put('http://localhost:9200/megacorp/employee/%s' % did,json.dumps(emp))
    print r
    assert r.ok


def main():
    add_employee(1,create_employee("John","Smith",25,"I love to go rock climbing",['sports','music']))
    add_employee(2,create_employee("Jane","Smith",32,"I like to collect rock albums",['music']))
    add_employee(3,create_employee("Douglas","Fir",35,"I like build cabinets",['fostery']))
    

if __name__ == '__main__':
    main()



    
