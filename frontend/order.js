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
<tbody>
    <tr v-for="order in orders">
        <td>{{order.order_id__order_name}}</td>
        <td>{{order.order_id__customer_id__company_id__company_name}}</td>
        <td>{{order.order_id__customer_id__user_id}}</td>
        <td>{{order.date}}</td>
        <td>{{order.deliveries__delivered_quantity || 0}}</td>
        <td>{{order.quantity}}</td>

    </tr>
</tbody>
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


    console.log("================")
    
    console.log("==========end====")
 

