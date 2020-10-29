<template>
  <div class="addTaskModal" v-show="ifAdd">
    <div class="container">
      <div class="container upper-panel">
        <div></div>
        <div class="dodaj">Dodaj zadanie</div>
        <a class="delete" @click="closeModal"></a>
      </div>
      <div class="field">
        <div class="control padding-text-area">
          <textarea class="textarea has-fixed-size" placeholder="Max 5 rows of tasks" rows="7"></textarea>
        </div>
      </div>
      <div class="field ohoho">
        <div class="control">
          <button class="button is-primary" @click="getTaskMessage">OK</button>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "AddTaskModal",
  props: {
    ifAdd: {
      Type: Boolean,
      required: true
    }
  },
  data() {
    return {
      huj: []
    };
  },
  methods: {
    /* eslint-disable no-mixed-spaces-and-tabs */
    getTaskMessage() {
      let text = document.querySelector("textarea").value;
      if (text === "") {
        this.$store.state.modalAppear = false;
      } else {
        fetch("http://127.0.0.1:5000/addTask", {
          method: "POST",
          mode: "no-cors", // no-cors, *cors, same-origin
          cache: "no-cache",
          credentials: "same-origin", // include, *same-origin, omit
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify(text)
        });
        let vm = this;

        let ddd = async () => {
          /* eslint-disable */
          let ggg = [];
          let old_length = vm.$store.state.allTask.length;
          while (true) {
            let bbb = 0;
            ggg = await fetch(`http://127.0.0.1:5000/`).then(data =>
              data.json()
            );
            bbb = ggg.length;
            if (old_length !== 0) {
              if (bbb !== old_length) break;
            }
            if (old_length === 0) {
              if (ggg.length !== 0) break;
            }
            console.log(ggg);
          }
          vm.$store.state.allTask = ggg;
          vm.$store.state.taskLength = ggg.length - 1;
        };
        ddd();
        this.$store.state.modalAppear = false;
        document.querySelector("textarea").value = "";
      }
    },
    closeModal() {
      this.$store.state.modalAppear = false;
    }
  }
};
</script>
<style scoped>
.addTaskModal {
  position: absolute;
  top: 20%;
  background-color: lightgrey;
  width: 50%;
  border-radius: 5px;
}
.delete{
  margin:.8rem;
}

.dodaj {
  font-size: 1.5rem;
  padding: 0.5rem;
}
.upper-panel {
  display: flex;
  justify-content: space-between;
}
.button{
  margin-bottom: 1.5rem;
}
textarea {
  border: none;
}

.ohoho {
  margin-top: 1rem;
  width: 25%;
  margin-left: auto;
  margin-right: auto;
}

.ohoho > .control > button {
  width: 100%;
}

.padding-text-area {
  padding: .8rem;
  box-sizing: border-box;
}
</style>