const store = new Vuex.Store({
    state: {
        title: 'ToDo Items',
        items: [],
    },
    mutations: {
        set_data(state, items) {
            state.items = items
        },
    },
    actions: {
        load_data(context) {
            Vue.http.get('/api/todos/', {responseType: 'json'}).then(resp => {
                context.commit('set_data', resp.body)
            });
        },
        add_todo(context, todo) {
            Vue.http.post('/api/todos/', {description: todo.description}).then(response => {
                context.dispatch('load_data')
            });
        },
        update_todo(context, todo) {
            Vue.http.patch('/api/todos/'+todo.uuid+'/', {completed_at: todo.completed_at}).then(response => {
                context.dispatch('load_data')
            });
        },
        delete_todo(context, uuid){
            Vue.http.delete('/api/todos/'+uuid+'/').then(response => {
                context.dispatch('load_data')
            });
        }
    }
})

Vue.component('todo_item_component', {
    template: `
    <div class="row list-group-item-action">
        <div class="col-md-1"><input type="checkbox" v-on:click="complete_todo" :checked="item.completed_at" /></div>
        <div class="col-md-10">{{ item.description }}</div>
        <div class="col-md-1"><a href="#" v-on:click.stop="delete_todo"> [X] </a></div>
    </div>
        `,
    props: ['item'],
    methods: {
        complete_todo() {
            var completed_at = new Date().toISOString();
            if (this.item.completed_at){
                completed_at = null;
            }
            store.dispatch('update_todo', {uuid: this.item.uuid, completed_at: completed_at});
        },
        delete_todo() {
            store.dispatch('delete_todo', this.item.uuid);
        }
    }
});

var todo_app = new Vue({
    el: "#todo-app",
    delimiters: ['${', '}'],
    store,
    mounted() {
        store.dispatch('load_data')
    },
    computed: Vuex.mapState({
        title: state => state.title,
        items: state => state.items
    }),
    methods: {
        create() {
            description = this.$refs.new_text.value;
            if (!description) {
                alert('Please enter description');
                return;
            }
            store.dispatch('add_todo', {'description': description})
            this.$refs.new_text.value = '';
        }
    }
});
