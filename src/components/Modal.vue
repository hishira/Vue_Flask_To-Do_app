<template>
    <div class='center-modal'>
        <section class="hero is-succes is-flex">
            <div>
                <div v-for="item in getTasks" :key="item[0]" class='card is-medium'>
                    <header class='card-header'>
                        <p class='card-header-title'>
                            Zadanie
                        </p>
                        <a class='card-header-icon' aria-label='more-options'>
                            <span class="icon">
                                <i class="fas fa-angle-down" aria-hidden="true"></i>
                            </span>
                        </a>
                    </header>
                    <div class='card-content'>
                        <div class='content'>
                            {{item[1]}}
                        </div>
                    </div>
                    <Buttons :taskid='item[0]' @taskRemove='deleteTask'  />
                </div>
            </div>
        </section>
    </div>
</template>
<script>
import Buttons from './ButtonComp.vue'

export default {
    name: 'Modal',
    components: {
        Buttons
    },props:{
        additionalTask:{
            type: Array,
            required: false
        }
    },
    computed:{
        getTasks(){
            return this.$store.state.allTask
        }
    },
    data() {
        return {
            tasks: []
        }
    },
    methods: {
        deleteTask(taskId) {
            console.log(taskId)
            let vm = this
            //const apiURL = `http://127.0.0.1:5000/removeTask/${taskId}`
            fetch(`http://127.0.0.1:5000/removeTask/${taskId}`, { method: "POST" })
                .then(dane => dane.json())
                .then(dane => {
                    vm.tasks = dane
                    vm.$store.state.allTask = dane
                })
        },
    },
    created() {
        let vm = this
        fetch('http://127.0.0.1:5000/')
            .then(data => data.json())
            .then(data => {
                vm.tasks = data
                vm.$store.state.allTask = data
            })
    }

}
</script>
<style scoped>
.center-modal {
    
}
.card{
    width: 25rem;
    border-radius: 15px;
}
</style>