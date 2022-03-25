var root = document.getElementById('root');

const TodoData = {
    entries: [],

    loadTodos: function () {
        m.request({
            method: "GET",
            url: "/api/v1/todo/",
        })
            .then(function (data) {
                TodoData.entries = [...TodoData.entries, ...data]
            })
    }

}

const TodoListComponent = {
    oncreate: function () {
        TodoData.loadTodos()
    },

    view: function () {
        return m("div", { className: "todo__list" }, [
            m(
                "ul",
                TodoData.entries.map(entry => {
                    return m(
                        "li",
                        {
                            className: 'todo__task'
                        },
                        entry.text
                    );
                })
            )
        ])
    }
}


m.mount(root, TodoListComponent)
