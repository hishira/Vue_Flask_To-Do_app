<template>
    <section class="hero is-primary is-fullheight is-flex">
        <div class="hero-head">
            <nav class="navbar">
                <div class="container">
                    <div class="navbar-brand">
                        <a class="navbar-item">
                            <img src="https://i.pinimg.com/originals/0d/8d/07/0d8d07a763e83f93acf810ae2c523bd7.png" alt="Logo">
                        </a>
                    </div>
                    <div id='nav-menu' class="navbar-menu is-flex">
                        <div class="navbar-end">
                            <a class="navbar-item is-active">
                                Home
                            </a>
                            <a class="navbar-item">
                                Other
                            </a>
                        </div>
                    </div>
                </div>
            </nav>
        </div>
        <div class="hero-body is-fluid">
            <div class="container">
                <Modal />
            </div>
            <div class='container'>
                <button class='button is-success' @click='addTask'>Dodaj zadanie</button>
            </div>
            <TaskModal :ifAdd='ifModal'  />
        </div>
        <div class="hero-foot footer-margin">
            <div class="container has-text-centered ">
                <i>Michał Skorupa</i> <i>{{new Date().toJSON().slice(0,10).replace(/-/g,'/')}}</i>
            </div>
        </div>
    </section>
</template>
<script>
import Modal from './Modal.vue'
import TaskModal from './AddTaskModal.vue'

export default {
    name: 'MainView',
    components: {
        Modal,
        TaskModal
    },
    data(){
      return{
        
      }
    },computed:{
      ifModal(){
        return this.$store.state.modalAppear
    }
  },
    methods:{
      addTask(){
        this.$store.state.modalAppear = true;
      },
      methodForClose(ee){
        this.$store.state.modalAppear = ee;
      }
    }

}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.hero-body {
    flex-direction: column;
    box-sizing: border-box;
    margin: 0;
}

.hero-head {
    //border-bottom: 1px solid #615e61;
    border-raius: 15px;
    box-shadow: 0px 6px 18px -4px #615e61;

}

.footer-margin {
    padding: -1rem;
    box-sizing: border-box;

}
</style>