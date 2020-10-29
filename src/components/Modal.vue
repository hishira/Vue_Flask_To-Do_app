<template>
  <div class="center-modal">
    <section class="hero is-succes is-flex">
      <div v-show="loading">
        <div v-for="item in getTasks" :key="item['_id']" class="card is-medium">
          <header class="card-header">
            <p class="card-header-title">Zadanie</p>
            <a class="card-header-icon" aria-label="more-options">
              <span class="icon">
                <i class="fas fa-angle-down" aria-hidden="true"></i>
              </span>
            </a>
          </header>
          <div class="card-content">
            <div class="content">
              {{ item["tresc_zadania"] }}
            </div>
          </div>
          <Buttons
            :taskid="item['_id']"
            @taskRemove="deleteTask"
            @updateTask="updatetask"
          />
        </div>
      </div>
    </section>
  </div>
</template>
<script>
import Buttons from "./ButtonComp.vue";

export default {
  name: "Modal",
  components: {
    Buttons,
  },
  props: {
    additionalTask: {
      type: Array,
      required: false,
    },
    lastSite: {
      type: Number,
      requred: true,
    },
    currentSite: {
      type: Number,
      requried: true,
    },
  },
  computed: {
    getTasks() {
      return this.$store.state.allTask.slice(
        this.$props.lastSite,
        this.$props.currentSite + 1
      );
    },
  },
  data() {
    return {
      tasks: [],
      loading: false,
    };
  },
  methods: {
    async deleteTask(taskId) {
      console.log(taskId);
      let data = await fetch(`http://127.0.0.1:5000/removeTask/${taskId}`, {
        method: "POST",
      }).then((dane) => dane.json())
      this.$data.tasks = data;
      this.$store.state.allTask = data;
      this.$store.state.taskLength = data.length - 1;
    },
    updatetask(taksID) {
      console.log(taksID);
      this.$emit("taskToUpdate", taksID);
    },
    async fetchData() {
      let vm = this;
      try {
        let data = await fetch("http://127.0.0.1:5000/", {
          method: "GET",
        }).then((response) => response.json());
        if (data === false) throw new Error("error");
        console.log(data);
        this.$data.loading = true;
        this.$data.tasks = data;
        vm.$store.state.allTask = data;
        vm.$store.state.taskLength = data.length - 1;
      } catch (e) {
        console.log(e);
        this.$data.loading = false;
      }
    },
  },
  created() {
    this.fetchData();
  },
};
</script>
<style scoped>
.center-modal {
}
.hero {
  position: relative;
}
.card {
  width: 25rem;
  border-radius: 15px;
}
</style>