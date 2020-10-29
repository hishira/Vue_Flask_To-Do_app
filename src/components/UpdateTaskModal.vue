/* eslint-disable*/
<template>
  <div class="addTaskModal" v-show="ifUpdate">
    <div class="container">
      <div class="container upper-panel">
        <div></div>
        <div class="dodaj">Aktualizuj zadanie</div>
        <a class="delete" @click="closeModal"></a>
      </div>
      <div class="field">
        <div class="control padding-text-area">
          <textarea
            id="mytextArea"
            class="textarea has-fixed-size"
            placeholder
            rows="7"
          ></textarea>
        </div>
      </div>
      <div class="field ohoho">
        <div class="control">
          <button class="button is-primary" @click="updateTask">OK</button>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
/* eslint-disable no-mixed-spaces-and-tabs */
export default {
  name: "UpdateTaskModal",
  props: {
    ifUpdate: {
      Type: Boolean,
      required: true,
    },
    stringToUpdate: {
      Type: String,
      required: true,
    },
    taskId: {
      Type: String,
      required: true,
    },
  },
  data() {
    return {
      huj: [],
    };
  },
  methods: {
    /* eslint-disable no-mixed-spaces-and-tabs */
    async updateTask() {
      let text = document.getElementById("mytextArea").value;
      console.log(text);
      console.log(this.$props.taskId);
      if (text === "") {
        this.$store.state.updateModalAppear = false;
      } else {
        let fetchobject = {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(text),
        };
        let url =`http://127.0.0.1:5000/update/${this.$props.taskId}`;
        let data = await fetch(url,fetchobject).then((response) => response.json());

        this.$store.state.allTask = data;
        this.$store.state.updateModalAppear = false;
      }
    },
    closeModal() {
      this.$store.state.updateModalAppear = false;
    },
  },
};
</script>
<style scoped>
.addTaskModal {
  position: absolute;
  top: 20%;
  background-color: lightgrey;
  width: 50%;
  z-index: 200;
  border-radius: 5px;
}
.button {
  margin-bottom: 1.5rem;
}
.dodaj {
  font-size: 1.5rem;
  padding: 0.5rem;
}
.delete {
  margin: 0.8rem;
}
.upper-panel {
  display: flex;
  justify-content: space-between;
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
  padding: 0.8rem;
  box-sizing: border-box;
}
</style>