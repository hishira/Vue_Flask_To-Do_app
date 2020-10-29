<template>
  <section class="hero is-primary is-fullheight is-flex">
    <div class="hero-head">
      <nav class="navbar">
        <div class="">
          <div class="navbar-brand">
            <a class="navbar-item">
              <img
                src="https://i.pinimg.com/originals/0d/8d/07/0d8d07a763e83f93acf810ae2c523bd7.png"
                alt="Logo"
              />
            </a>
          </div>
        </div>
      </nav>
    </div>
    <div class="hero-body is-fluid">
      <div class="cnttmp">
        <Modal @taskToUpdate="updateTask" :currentSite="currentSite" :lastSite="lastSite" />
      </div>
      <TaskModal :ifAdd="ifModal" />
      <UpdateModal :ifUpdate="ifUpdateModal" :stringToUpdate="getTaskToUpdate" :taskId="getTaskID" />
      <nav v-show="checkLength > 1" class="pagination" role="navigation" aria-label="pagination">
        <a class="pagination-previous" style="background-color:azure" @click="previousPage">Previous</a>
        <a class="pagination-next" style="background-color:azure" @click="nextPage">Next page</a>
      </nav>
    </div>
    <div class="button-class">
      <div class="container">
        <button class="button is-success" @click="addTask">Dodaj zadanie</button>
      </div>
    </div>
    <div class="hero-foot footer-margin">
      <div class="container has-text-centered">
        <i>Michał Skorupa</i>
        <i>
          {{
          new Date()
          .toJSON()
          .slice(0, 10)
          .replace(/-/g, "/")
          }}
        </i>
      </div>
    </div>
  </section>
</template>
<script>
import Modal from "./Modal.vue";
import TaskModal from "./AddTaskModal.vue";
import UpdateModal from "./UpdateTaskModal.vue";
export default {
  name: "MainView",
  components: {
    Modal,
    TaskModal,
    UpdateModal
  },
  data() {
    return {
      taskToUpdate: "",
      taskID: "",
      lastSite: 0,
      currentSite: 1,
      maxTaskPerSite: 2
    };
  },
  computed: {
    ifModal() {
      return this.$store.state.modalAppear;
    },
    ifUpdateModal() {
      return this.$store.state.updateModalAppear;
    },
    getTaskToUpdate() {
      return this.taskToUpdate;
    },
    getTaskID() {
      return this.taskID;
    },
    checkLength() {
      return this.$store.state.allTask.length;
    }
  },
  methods: {
    addTask() {
      this.$store.state.modalAppear = true;
    },
    nextPage() {
      if (this.lastSite < this.$store.state.taskLength) {
        this.lastSite += 1;
        this.currentSite += 1;
      }
    },
    previousPage() {
      if (this.lastSite - 1 >= 0) {
        this.lastSite -= 1;
        this.currentSite -= 1;
      }
    },
    methodForClose(ee) {
      this.$store.state.modalAppear = ee;
    },
    updateTask(taskId) {
      for (let i of this.$store.state.allTask) {
        if (i["_id"] === taskId) {
          this.taskToUpdate = i["tresc_zadania"];
          this.taskID = taskId;
          break;
        }
      }
      this.$store.state.updateModalAppear = true;
    }
  }
};
</script>
<style scoped>
.hero-body {
  flex-direction: column;
  box-sizing: border-box;
  margin: 0;
}
.button-class {
  padding: 2rem;
}

.hero-head {
  border-radius: 15px;
  box-shadow: 0px 6px 18px -4px #615e61;
}

.footer-margin {
  padding: -1rem;
  box-sizing: border-box;
}
.navbar-item{
  margin-left: .5rem;

}
.cnttmp{
  width: 100%;
  margin-bottom: 2.5rem;
}
</style>
