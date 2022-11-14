const order = {template: `
<table id="my-table" class ="table table-striped">

<thead>
    <tr>
        <th>
            Order Name
        </th>
        <th>
            Customer Company
        </th>
        <th>
            Customer Name
        </th>
        <th>
            Order Date
        </th>
        <th>
            Delivered Amount
        </th>
        <th>
            Total Amount
        </th>
    </tr>
</thead>

</table>
`,

data(){
    return {
        orders:[],
    }
},
methods:{
    getnewData(){
        axios.get('http://127.0.0.1:8000/orders')
        .then((response)=>{
            // console.log(response.data);
            data = JSON.parse(response.data)
            
            this.orders = data;
            console.log(typeof(data))
            console.log(data)
            
            function getColumns(){
                for(var i = 0; i < data.length; i++){
                  let columnsArray = [];
                  var keys = Object.keys(data[i]);
                  for(k in Object.keys(data[i])){
                    if(data[i].hasOwnProperty(keys[k])){
                      columnsArray.push({
                          "data":keys[k]
                      });
                    }
                  }
                  return columnsArray;
                }
            }
            var table = $('#my-table').DataTable({
                columnDefs: [{
                    "defaultContent": "-",
                    "targets": "_all"
                  }],                
                "lengthChange": false,
                "columns": getColumns(),
                "data": data,
                "pageLength" : 5 
          });         
        });
    },
    nextPage () {
        if(this.currentPage < Math.floor(this.orders.length/5)) {this.currentPage++; console.log("next page")};
      },
    prevPage:function() {
        if(this.currentPage > 1) this.currentPage--;
      },
   
   
},
mounted:function(){
    this.getnewData();
    }
}

