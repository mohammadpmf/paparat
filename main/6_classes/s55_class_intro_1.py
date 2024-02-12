students_names      = ['Ali'        , 'Reza'    , 'Sara'    , 'Nazanin' , 'Sara'    ]
students_surnames   = ['Rezayi'     , 'Hashemi' , 'Nadimi'  , 'Heshmati', 'Alavi'   ]
students_ids        = ['1563252'    , '2583255' , '3563715' , '7563455' , '8563155' ]
students_grades     = [19           , 14        , 18        , 19.5      , 9.5       ]

students_list = [
    {
        'name'      : 'Ali'     ,
        'surname'   : 'Rezayi'  ,
        'id'        : '1563252' ,
        'grade'     : 19        ,
    },
    {
        'name'      : 'Reza'    ,
        'surname'   : 'Hashemi' ,
        'id'        : '2583255' ,
        'grade'     : 14        ,
    },
    {
        'name'      : 'Sara'    ,
        'surname'   : 'Nadimi'  ,
        'id'        : '3563715' ,
        'grade'     : 18        ,
    },
     {
        'name'      : 'Nazanin' ,
        'surname'   : 'Heshmati',
        'id'        : '7563455' ,
        'grade'     : 19.5      ,
    },
     {
        'name'      : 'Sara'    ,
        'surname'   : 'Alavi'   ,
        'id'        : '8563155' ,
        'grade'     : 9.5       ,
    }
]

students_dict = {
    'ali': {
        'name'      : 'Ali'     ,
        'surname'   : 'Rezayi'  ,
        'id'        : '1563252' ,
        'grade'     : 19        ,
    },
    'reza': {
        'name'      : 'Reza'    ,
        'surname'   : 'Hashemi' ,
        'id'        : '2583255' ,
        'grade'     : 14        ,
    },
    'sara': {
        'name'      : 'Sara'    ,
        'surname'   : 'Nadimi'  ,
        'id'        : '3563715' ,
        'grade'     : 18        ,
    },
    'nazanin': {
        'name'      : 'Nazanin' ,
        'surname'   : 'Heshmati',
        'id'        : '7563455' ,
        'grade'     : 19.5      ,
    },
    'sara2': {
        'name'      : 'Sara'    ,
        'surname'   : 'Alavi'   ,
        'id'        : '8563155' ,
        'grade'     : 9.5       ,
    }
}


class Student:
    def __init__(self,name,surname,id,grade) -> None:
        self.name    = name
        self.surname = surname
        self.id      = id
        self.grade   = grade

ali     = Student('Ali'    , 'Rezayi'  ,'1563252', 19  )
reza    = Student('Reza'   , 'Hashemi' ,'2583255', 14  )
sara    = Student('Sara'   , 'Nadimi'  ,'3563715', 18  )
nazanin = Student('Nazanin', 'Heshmati','7563455', 19.5)
sara2   = Student('Sara'   , 'Alavi'   ,'8563155', 9.5 )

print(sara2.grade)

