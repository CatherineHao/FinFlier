<!--
 * @Description: 
 * @Author: Qing Shi
 * @Date: 2023-07-10 18:18:22
 * @LastEditors: Qing Shi
 * @LastEditTime: 2023-07-17 10:59:11
-->
<template>
    <div style="height: 100%; width: 100%;">
        <div style="font-family: KoHo; text-align: start; font-size: 22px;height: 40px; font-weight: bold;">
            
            <img src="../assets/img/2.png" width="25" alt=""> &nbsp;Data Description
            <hr>
        </div>
        <div style="height: calc(100% - 40px); widows: 100%; overflow-y: auto;">
            <div style="height: 100%; width: 100%; padding-top: 40px;">

                <div v-for="(item, item_i) in textGroup" :key="'group_' + item_i" :id="'group_' + item_i" :style="{
                    'transition': '1s', 'padding-top': '5px', 'padding-bottom': '5px', 'opacity': 1
                }">
                    <div style="width: 100%; display: flex;">
                        <div v-if="item.tag == 0" style=" width: 40px; padding-top: 3px; padding-left: 0px;">
                            <div
                                style="background-color: rgb(91, 155, 255); width: 35px; height: 35px; border-radius: 6px; padding: 4px;">
                                <svg v-if="item.tag == 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"
                                    fill="#FFF">
                                    <path d="M0 0h24v24H0z" fill="none" />
                                    <path
                                        d="M19 4h-4L7.11 16.63 4.5 12 9 4H5L.5 12 5 20h4l7.89-12.63L19.5 12 15 20h4l4.5-8z" />
                                </svg>
                                <svg v-else xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="#FFF">
                                    <path d="M0 0h24v24H0z" fill="none" />
                                    <path
                                        d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z" />
                                </svg>
                            </div>
                        </div>
                        <div style="width: calc(100% - 40px);">
                            <div v-if="item.tag"
                                style="width: 100%; line-height:1lh; text-align: start; padding: 8px; background-color: rgb(173, 216, 230, 0); border-radius:5px; min-height: 40px; border: 1px solid rgba(0, 0, 0, .3);" >
                                <span v-for="(o, i) in item.outputTextArray" :key="'res_' + i"
                                    :class="{ 'dataObject': o.tag == 1 }" :style="{
                                        backgroundColor: o.color
                                    }" @click="hoverObject(o)">{{ o.s }}</span>
                            </div>
                            <div v-else
                                style="width: 100%; line-height:1lh; text-align: start; padding-right: 5px; background-color: rgb(173, 216, 230, 0); padding: 8px; border-radius: 5px; border: 1px solid rgba(0, 0, 0, .3);">
                                {{ item.text }}
                            </div>
                        </div>

                        <div v-if="item.tag == 1" style="padding-top: 3px; padding-left: 0px; width: 40px;">
                            <div
                                style="background-color: rgb(91, 155, 255); width: 35px; height: 35px; border-radius: 6px; padding: 4px; float: right;">
                                <svg v-if="item.tag == 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"
                                    fill="#FFF">
                                    <path d="M0 0h24v24H0z" fill="none" />
                                    <path
                                        d="M19 4h-4L7.11 16.63 4.5 12 9 4H5L.5 12 5 20h4l7.89-12.63L19.5 12 15 20h4l4.5-8z" />
                                </svg>
                                <svg v-else xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="#FFF">
                                    <path d="M0 0h24v24H0z" fill="none" />
                                    <path
                                        d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z" />
                                </svg>
                            </div>

                        </div>
                    </div>

                </div>
            </div>
            <div style="text-align: start; position: absolute; top: 0px; width: 100%;">
                <div style="height: 100%; width: 100%; display: flex;">
                    <div style="width: calc(100% - 40px)">
                        <el-input v-model="inputText" autosize type="textarea" placeholder="Send a message"
                            style="width: 100%;" :autosize="{ minRows: 1, maxRows: 4 }" @keydown.enter="submitText()" />
                    </div>
                    <div style="width: 40px;">
                        <transition name="fade">
                            <button :class="['btn', { 'btn-green': hasInput }]" @click="submitText()">
                                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="none"
                                    class="h-4 w-4 m-1 md:m-0" stroke-width="2">
                                    <path
                                        d="M.5 1.163A1 1 0 0 1 1.97.28l12.868 6.837a1 1 0 0 1 0 1.766L1.969 15.72A1 1 0 0 1 .5 14.836V10.33a1 1 0 0 1 .816-.983L8.5 8 1.316 6.653A1 1 0 0 1 .5 5.67V1.163Z"
                                        :fill="hasInput == 1 ? 'white' : 'rgba(0, 0, 0, 0.2)'"></path>
                                </svg>
                            </button>
                        </transition>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import { useDataStore } from "../stores/counter";
import description_data from "@/assets/data/description.json"
export default {
    name: "DataTable",
    props: [],
    data () {
        return {
            inputText: '',
            outputText: '',
            outputTextArray: [],
            textGroup: [],
            objectTag: {}
        };
    },
    methods: {
        colorTrans (color) {
            return `rgba(${color.r}, ${color.g}, ${color.b}, ${color.a})`
        },
        submitText () {
            this.inputText = this.inputText.trim();
            let inputText = this.inputText;
            let outputText = '';
            let outputTextArray = [];
            this.inputText = '';
            let startPos = 0;
            let endPos = 0;
            this.textGroup.push({
                tag: 0,
                text: inputText,
                opacity: 0,
                outputTextArray: []
            });
            console.log(description_data)
            for (let i in description_data) {
                // console.log(this.colorTrans(description_data[i].color), description_data[i].color);
                let range = description_data[i].objectRange;
                endPos = range[0];
                let s = inputText.slice(startPos, endPos)
                outputText += s;
                outputText += `<span class="dataObject" style="background-color: ${this.colorTrans(description_data[i].color)};">` + description_data[i].objectText + `</span>`;
                outputTextArray.push({
                    s: s,
                    tag: 0
                });
                outputTextArray.push({
                    s: description_data[i].objectText,
                    tag: 1,
                    color: this.colorTrans(description_data[i].color),
                    rawColor: description_data[i].color,
                    objectName: description_data[i].objectName,
                    tableIndex: description_data[i].tableIndex
                })
                startPos = range[1];
            }
            endPos = inputText.length;
            let s = inputText.slice(startPos, endPos)
            outputText += s;
            this.outputText = outputText;
            this.outputTextArray = outputTextArray;
            this.textGroup.push({
                tag: 1,
                text: '',
                opacity: 0,
                outputTextArray: outputTextArray
            });
            // console.log(this.outputTextArray)
        },
        hoverObject (o) {
            // console.log(o, this.objectTag);
            if (this.objectTag[o.objectName] == 1) {
                this.outObject(o.objectName);
                return
            }
            // console.log(objectName);
            const dataStore = useDataStore();
            let objectTag = dataStore.objectTag;
            let tableTag = {};
            for (let i in o.tableIndex) {
                console.log(o.color)
                tableTag['cellR' + (o.tableIndex[i][0]).toString() + 'C' + (o.tableIndex[i][1]).toString()] = {
                    tag: 1,
                    color: o.color
                };
            }
            dataStore.selectTable = tableTag;
            // console.log(tableTag)
            this.tableTag = tableTag;
            objectTag[o.objectName] = 1;
            dataStore.objectTag = objectTag;
            this.objectTag = objectTag;

            let tmp = dataStore.type_chart_setting.overlayFormat;

            for (let i in tmp) {
                tmp[i].currentColor = o.rawColor;
            }
            // console.log(dataStore.state_map['stage0']['overlay_setting'], o.objectName);


            dataStore.state_map['state0']['overlay_setting'][o.objectName] = tmp;
            console.log(dataStore.state_map['state0']['overlay_setting']);
            // console.log(objectTag, dataStore.objectTag)
        },
        outObject (objectName) {
            const dataStore = useDataStore();
            let objectTag = dataStore.objectTag;
            objectTag[objectName] = 0;
            for (let i in this.tableTag) {
                this.tableTag[i].tag = 0;
            }
            dataStore.selectTable = this.tableTag;
            dataStore.objectTag = objectTag;
        }
    },
    watch: {
        inputText (newVal, oleVal) {
            this.inputText = this.inputText.trim();
        },
        textGroup: {
            handler (newVal, oleVal) {
                // console.log(this.textGroup.length);
                setTimeout(() => {
                    document.getElementById('group_' + (this.textGroup.length - 2)).style.opacity = 1;
                }, 500);

                setTimeout(() => {
                    document.getElementById('group_' + (this.textGroup.length - 1)).style.opacity = 1;
                }, 2000);
            },
            deep: true
        }
    },
    created () {
    },
    mounted () {
        this.inputText = "Investment by British investors accounted for 18 percent of new foreign direct investment expenditures. The Netherlands ($43.1 billion) was the second-largest investing country, followed by France ($35.3 billion)."
        this.submitText();

    },
    computed: {
        hasInput () {
            return this.inputText.trim() !== '';
        }
    },
    components: {}
}
</script>
<style>
.dataObject {
    border: 1px solid rgba(0, 0, 0, 0);
    border-radius: 3px;
    font-weight: bold;
    cursor: pointer;
    transition: 0.4s;
}

@media (hover: hover) {
    .dataObject:hover {

        border: 1px solid rgba(0, 0, 0, 1);
    }
}

.btn {
    height: 31px;
    width: 31px;
    /* border: 1px solid rgba(0, 0, 0, 0.2); */
    padding: 6px;
    float: right;
    border-radius: 6px;
}

.btn-green {
    border: 1px solid rgb(91, 155, 255);
    background-color: rgb(91, 155, 255);
}

.data_content {
    /* justify-content: center;
    align-items: center;
    display: -webkit-flex; */
}

/* .el-loading-spinner {
    background-color: black;
} */
</style>
