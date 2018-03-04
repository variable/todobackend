class ToDo{
    constructor(id, description, priority, completed_at){
        this.id = id;
        this.description = description;
        this.priority = priority;
        this.completed_at = completed_at;
    }
    save(){
        if (this.id){
            // Put
        } else {
            // Post
        }
    }
}

Vue.component('todo_item_component', {
    template: '<li><input type="checkbox" v-on:click="update"/>{{ item.description }}</li>',
    props: ['item'],
    methods: {
        update(){
           var date = Date();
           console.log(this.item);
           this.$http.patch('/todo/api/'+this.item.uuid+'/', {completed_at:date.dateString}).then(alert(1));
        }
    }
});

var todo_app = new Vue({
    el: "#todo-app",
    delimiters: ['${', '}'],
    data: {
        title: 'ToDo Items',
        items: [],
    },
    mounted() {
        var self = this;
        this.$http.get('/api/todos/', {responseType: 'json'}).then(resp=>{
            self.items=resp.body;
        });
    },
    methods: {
        create () {
            description = this.$refs.new_text.value;
            if (!description) {alert('Please enter description'); return;}
            this.$http.post('/api/todos/', {description:description}).then(response=>{}, response=>{console.log(response.body)});
        }
    }
});
