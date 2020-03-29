/* eslint-disable*/
<template>
    <div class='addTaskModal' v-show='ifUpdate'>
        <div class='container'>
            <div class='container upper-panel'>
                <div></div>
                <div class='dodaj'>Aktualizuj zadanie</div>
                <a class="delete" @click='closeModal'></a>
            </div>
            <div class='field'>
                <div class='control padding-text-area'>
                    <textarea id='mytextArea' class='textarea has-fixed-size' placeholder='' rows='7'></textarea>
                </div>
            </div>
            <div class='field ohoho'>
                <div class='control'>
                    <button class='button is-primary' @click='updateTask'>OK</button>
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
            required: true
        },
        stringToUpdate: {
            Type: String,
            required: true
        },
        taskId: {
            Type: Number,
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
        updateTask() {
            let text = document.getElementById('mytextArea').value
            console.log(text)
            console.log(this.$props.taskId)
            if (text === "") {
                this.$store.state.updateModalAppear = false

            } else {
                console.log(this.$props.taskId)
                let vm = this
                fetch(`http://127.0.0.1:5000/update/${this.$props.taskId}`, {
                    method: "POST",
                    mode: 'no-cors', // no-cors, *cors, same-origin
                    cache: 'no-cache',
                    credentials: 'same-origin', // include, *same-origin, omit
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(text)
                })
                let i = 0
                while (i < 10) {
                    let dataCC = []
                    fetch('http://127.0.0.1:5000/')
                        .then(data => data.json())
                        .then(data => {
                            console.log(data)
                       		dataCC = data
                            vm.$store.state.allTask = data
                        })
                    for(let i of dataCC){
                    	if(i['zadanie_id'] === this.$props.taskId){
                    		if(i['tresc_zadania'] === text)
                    			break;
                    	}
                    }
                    i++;
                }
                this.$store.state.updateModalAppear = false
                /*
                let ddd = async () => {
                    /* eslint-disable */
                /*
                                    let ggg = []
                                    let old_length = vm.$store.state.allTask.length
                                    while (true) {
                                        let bbb = 0
                                        ggg = await fetch(`http://127.0.0.1:5000/`).then(data => data.json())
                                        bbb = ggg.length
                                        if (old_length !== 0) {
                                            if (bbb !== old_length)
                                                break
                                        }
                                        if (old_length === 0) {
                                            if (ggg.length !== 0)
                                                break
                                        }
                                        console.log(ggg)
                                    }
                                    vm.$store.state.allTask = ggg
                                }

                                //console.log(getjson)
                                //this.$store.state.allTask = getjson
                                this.$store.state.modalAppear = false
                                document.querySelector('textarea').value = ""
                                */
            }

        },
        closeModal() {
            this.$store.state.updateModalAppear = false
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

.delete {
    //align-self: center;

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

.ohoho>.control>button {
    width: 100%;


}

.padding-text-area {
    padding: 0 .5rem 0 .5rem;
    box-sizing: border-box;
}
</style>