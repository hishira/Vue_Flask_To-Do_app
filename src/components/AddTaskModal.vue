<template>
    <div class='addTaskModal' v-show='ifAdd'>
        <div class='container'>
            <div class='dodaj'>Dodaj zadanie</div>
            <a class="delete" @click='closeModal'></a>
            <div class='field'>
                <div class='control padding-text-area'>
                    <textarea class='textarea has-fixed-size' placeholder='Max 5 rows of tasks' rows='7'></textarea>
                </div>
            </div>
            <div class='field ohoho'>
                <div class='control'>
                    <button class='button is-primary' @click='getTaskMessage'>OK</button>
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
        }
    },
    methods: {
        /* eslint-disable no-mixed-spaces-and-tabs */
        getTaskMessage() {
            let text = document.querySelector('textarea').value
            if (text === "") {
                this.$store.state.modalAppear = false

            } else {
                fetch('http://127.0.0.1:5000/addTask', {
                    method: "POST",
                    mode: 'no-cors', // no-cors, *cors, same-origin
                    cache: 'no-cache',
                    credentials: 'same-origin', // include, *same-origin, omit
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(text)
                })

                let vm = this
                fetch(`http://127.0.0.1:5000/`)
                    .then(dane => dane.json())
                    .then(dane => {
                        console.log(dane)
                        vm.$store.state.allTask = dane
                    })
                event.preventDefault()
                this.$store.state.modalAppear = false
                document.querySelector('textarea').value = ""
            }

        },
        closeModal() {
            this.$store.state.modalAppear = false
        }
    }
}
</script>
<style scoped>
.addTaskModal {
    position: absolute;
    top: 20%;
    background-color: lightgrey;
    width: 50%;
    height: 50%;
    border-radius: 5px;
}

.dodaj {
    font-size: 1.5rem;
    padding: .5rem;
}

textarea {
    border: none;
}

.ohoho {
    margin-top: 1rem;
    border: 2px solid red;
    width: 25%;
    margin-left: auto;
    margin-right: auto;
}

.ohoho>.control>button {
    width: 100%;


}

.padding-text-area {
    padding: 0 .5rem 0 .5rem;
    box-sizing: border-box;
}
</style>