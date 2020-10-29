<template>
    <footer class='card-footer'>
        <a class='card-footer-item' @click='updateTask'>
            Zaaktualizuj
        </a>
        <a class='card-footer-item' @click='deleteClick'>
            Usuń
        </a>
    </footer>
</template>
<script>
export default {
    name: "Buttons",
    props: {
        taskid: {
            type: Number,
            required: true
        }
    },
    methods: {
        deleteClick() {
            this.$emit('taskRemove', this.$props.taskid)
        },
        updateTask(){
            this.$emit('updateTask',this.$props.taskid)
        }
    }
}
</script>
<style scoped>
</style>