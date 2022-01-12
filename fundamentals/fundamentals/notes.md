Javascript vs Python

Javascript

    var name = "Nolan"
    var someList = ["cookies", "tomatoes", "pies"]

    function nameOfFunction(name){
        if(name === "Nolan"){
            console.log("Yeah")
        }else if(name=== "Pablo"){
            console.log("Awesome")
        }
    }
    console.log("out of function")

    for(var i = 0; i <someList.length;i++){
        let item = someList[i]
    }

Python

    name = "Nolan"
    some_list = ["cookies", "tomatoes", "pies"]

    def name_of_function(name):
        print("Hello World")
        if name == "Nolan:
            print("Yeah")
        elif name == "Pablo":
            print("Awesome")

    print("out of function")

    for idx in range(len(some_list)):
        item = some_list[idx]

**Differences** - dont' have to put var to declare variable - Indentation is more important - snake case vs. camel case

\*\*A function becomes what it returns
