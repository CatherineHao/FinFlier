<template>
    <div>
        <div
            style="font-family: KoHo, 'operator Mono Lig'; font-size: 22px;  height: 40px; text-align: start; font-weight: bold;">

            <img src="../assets/img/4.png" width="25" alt="">&nbsp; Design Panel
            <hr>
        </div>
        <v-expand-transition>
            <div v-show="expand" style="overflow-y: auto; overflow-x: auto;">
                <div class="EditPanel">
                    <!-- <h3 class="background"><span>Canvas</span></h3>
                    <div class="EditInfo">
                        <div>Theme</div>
                    </div> -->
                    <el-collapse accordion>
                        <el-collapse-item name="1">
                            <template #title>
                                <el-checkbox v-model="checked1" label="Option 1" size="large" />
                            </template>
                            <div>
                                Consistent with real life: in line with the process and logic of real
                                life, and comply with languages and habits that the users are used to;
                            </div>
                            <div>
                                Consistent within interface: all elements should be consistent, such
                                as: design style, icons and texts, position of elements, etc.
                            </div>
                        </el-collapse-item>
                        <el-collapse-item title="Feedback" name="2">
                            <div>
                                Operation feedback: enable the users to clearly perceive their
                                operations by style updates and interactive effects;
                            </div>
                            <div>
                                Visual feedback: reflect current state by updating or rearranging
                                elements of the page.
                            </div>
                        </el-collapse-item>
                        <el-collapse-item title="Efficiency" name="3">
                            <div>
                                Simplify the process: keep operating process simple and intuitive;
                            </div>
                            <div>
                                Definite and clear: enunciate your intentions clearly so that the
                                users can quickly understand and make decisions;
                            </div>
                            <div>
                                Easy to identify: the interface should be straightforward, which helps
                                the users to identify and frees them from memorizing and recalling.
                            </div>
                        </el-collapse-item>
                        <el-collapse-item title="Controllability" name="4">
                            <div>
                                Decision making: giving advices about operations is acceptable, but do
                                not make decisions for the users;
                            </div>
                            <div>
                                Controlled consequences: users should be granted the freedom to
                                operate, including canceling, aborting or terminating current
                                operation.
                            </div>
                        </el-collapse-item>
                    </el-collapse>
                </div>
            </div>
        </v-expand-transition>
    </div>
</template>
<script>
import { useDataStore } from "../stores/counter";
export default {
    name: "DataTable",
    props: [],
    data () {
        return {
            checked1: 1,
            msg1: "Hello, main!",
            rawData: [],
            th: [],
            td: [],
            tableTag: {},
            expand: false
        };
    },
    methods: {
        // calcTable (data) {
        //     let th = data.columns;
        //     return [th, data];
        // }
    },
    created () {
    },
    computed: {
    },
    mounted () {
        const dataStore = useDataStore();
        this.rawData = dataStore.data;
        // [this.th, this.td] = this.calcTable(this.rawData);
        // console.log(this.rawData)
        setTimeout(() => this.expand = !this.expand, 100);
        dataStore.$subscribe(() => {
            // this.tableTag = dataStore.selectTable;
            // // console.log(this.tableTag);
            // for (let i in this.tableTag) {
            //     // console.log(this.);
            //     const element = document.getElementById(i);
            //         // console.log(element.style);
            //     if (this.tableTag[i].tag == 1) {
            //         element.style.backgroundColor = this.tableTag[i].color;
            //     } else {
            //         element.style.backgroundColor = 'white';
            //     }
            // }
            // console.log(this.tableTag, dataStore.selectTable)
        })
    },
    components: {}
}
</script>
<style scoped>
h3 {
    margin-top: 10px;
    text-align: center;
    text-transform: uppercase;
    background: #fff;

    font-family: "DM Sans", sans-serif;
    color: #2a2a2a;
    font-size: 16px;
    font-weight: 600;
    margin-bottom: 10px;
}

h3.background {
    position: relative;
    z-index: 1;

    &:before {
        border-top: 1px solid #2a2a2a;
        content: "";
        margin: 0 auto;
        /* this centers the line to the full width specified */
        position: absolute;
        /* positioning must be absolute here, and relative positioning must be applied to the parent */
        top: 50%;
        left: 0;
        right: 0;
        bottom: 0;
        width: 95%;
        z-index: -1;
    }

}

h3 span {
    /* to hide the lines from behind the text, you have to set the background color the same as the container */
    background: #fff;
    padding: 0 15px;
}

.EditInfo {
    text-align: start;
}
</style>
