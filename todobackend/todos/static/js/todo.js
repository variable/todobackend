Vue.component('todo_item_component', {
    template: '<li><input type="checkbox"/>{{ item.description }}</li>',
    props: ['item']
});

var todo_app = new Vue({
    el: "#todo-app",
    delimiters: ['${', '}'],
    data: {
        title: 'ToDo Items',
        items: [
            {
                uuid: 'uuid1',
                description: 'test1'
            },
            {
                uuid: 'uuid2',
                description: 'test2'
            },
        ]
    }
});
