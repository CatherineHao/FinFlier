<!--
 * @Description: 
 * @Author: Qing Shi
 * @Date: 2023-07-10 18:18:22
 * @LastEditors: Qing Shi
 * @LastEditTime: 2023-08-28 18:26:01
-->
<template>
    <div style="height: 100%; width: 100%;">
        <div style="font-family: KoHo; text-align: start; font-size: 22px;height: 40px; font-weight: bold;">

            <img src="../assets/img/2.png" width="25" alt=""> &nbsp;Data Description
            <hr>
        </div>
        <div style="height: calc(100% - 40px); widows: 100%;">
            <div style="text-align: start; position: absolute; top: 0px; width: 100%; height: 40px;">
                <div style="height: 100%; width: 100%; display: flex;">
                    <div style="width: calc(100% - 40px)">
                        <el-input v-model="inputText" type="textarea" placeholder="Send a message" style="width: 100%;"
                            :autosize="{ minRows: 1, maxRows: 4 }" />
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
            <div ref="scrollableDiv"
                style="position: absolute; top: 40px; height: calc(100% - 40px); width: 100%; overflow-y: auto;">
                <div v-for="(item, item_i) in textGroup" :key="'group_' + item_i" :id="'group_' + item_i" :style="{
                    'transition': '1s', 'padding-top': '5px', 'padding-bottom': '5px', 'opacity': 1
                }">
                    <div style="width: 100%; display: flex;">
                        <div v-if="item.tag == -1" style=" width: 40px; padding-top: 3px; padding-left: 0px;">
                            <div
                                style="background-color: rgb(91, 155, 255); width: 35px; height: 35px; border-radius: 6px; padding: 4px;">
                                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="#FFF">
                                    <path d="M0 0h24v24H0z" fill="none" />
                                    <path
                                        d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z" />
                                </svg>
                            </div>
                        </div>
                        <div style="width: calc(100% - 40px);">
                            <div v-if="item.tag == -1"
                                style="width: 100%; line-height:1lh; text-align: start; padding-right: 5px; background-color: rgb(173, 216, 230, 0); padding: 8px; border-radius: 5px; border: 1px solid rgba(0, 0, 0, .3);">
                                {{ item.text }}
                            </div>
                            <div v-else
                                style="width: 100%; line-height:1lh; text-align: start; padding: 8px; background-color: rgb(173, 216, 230, 0); border-radius:5px; min-height: 40px; border: 1px solid rgba(0, 0, 0, .3);">
                                <span v-for="(o, i) in item.outputTextGroup" :key="'res_' + i"
                                    :class="{ 'dataObject': o.tag != -1 }" :style="{
                                        backgroundColor: o.tag == 2 ? o.color + '4D' : 'white',
                                        'border-bottom': o.tag == 0 || o.tag == 2 ? '3px solid ' + o.color : '0px',
                                        'text-decoration-color': o.color
                                    }" @click="hoverObject(o)">{{ o.text }}</span>
                            </div>
                        </div>

                        <div v-if="item.tag == 1" style="padding-top: 3px; padding-left: 0px; width: 40px;">
                            <div
                                style="background-color: rgb(91, 155, 255); width: 35px; height: 35px; border-radius: 6px; padding: 4px; float: right;">
                                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="#FFF">
                                    <path d="M0 0h24v24H0z" fill="none" />
                                    <path
                                        d="M19 4h-4L7.11 16.63 4.5 12 9 4H5L.5 12 5 20h4l7.89-12.63L19.5 12 15 20h4l4.5-8z" />
                                </svg>
                            </div>

                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>
</template>
<script>
import { useDataStore } from "../stores/counter";
import description_data from "@/assets/data/test.json"
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
        scrollToBottom () {
            this.$refs.scrollableDiv.scrollTop = this.$refs.scrollableDiv.scrollHeight;
        },
        submitText () {
            this.inputText = this.inputText.trim();
            let inputText = this.inputText;
            console.log(description_data);
            this.inputText = "";
            let originalText = description_data[0]['OriginText'];
            // console.log(originalText);
            this.textGroup.push({
                tag: -1,
                text: originalText
            })
            this.$nextTick(() => {
                this.scrollToBottom();
            })
            let outputTextGroup = [];
            let startPos = 0;
            let endPos = 0;
            for (let i in description_data) {
                for (let j in description_data[i].ConversationInfo) {
                    let info = description_data[i].ConversationInfo[j];
                    let pos = []
                    if (typeof (info['Num']) == 'object') {
                        for (let k in info['Num']) {
                            pos.push({
                                pos: info['NumPosition'][k],
                                text: info['Num'][k],
                                tag: 0
                            })
                        }
                    }
                    if (typeof (info['Trend']) == 'object') {
                        for (let k in info['Trend']) {
                            pos.push({
                                pos: info['TrendPosition'][k],
                                text: info['Trend'][k],
                                tag: 1
                            })
                        }
                    }
                    if (typeof (info['ObjectName']) == 'object') {
                        for (let k in info['ObjectName']) {
                            pos.push({
                                pos: info['ObjectPosition'][k],
                                text: info['ObjectName'][k],
                                tag: 2
                            })
                        }
                    }
                    pos.sort((a, b) => a.pos[0] - b.pos[0])
                    for (let k in pos) {
                        endPos = pos[k].pos[0];
                        let s = originalText.slice(startPos, endPos);
                        console.log(startPos, endPos, s, "0")
                        if (startPos != endPos) {
                            console.log(s)
                            outputTextGroup.push({
                                text: s,
                                tag: -1,
                            })
                        }
                        startPos = pos[k].pos[0];
                        endPos = pos[k].pos[1] + 1;
                        s = originalText.slice(startPos, endPos);
                        console.log(startPos, endPos, s, "1")
                        outputTextGroup.push({
                            text: s,
                            tag: pos[k].tag,
                            color: description_data[i].color
                        });
                        startPos = endPos;
                    }
                }
                // outputTextGroup.push({
                //     tag: 
                // })

            }
            outputTextGroup.push({
                text: originalText.slice(startPos, originalText.length
                ),
                tag: -1,
                color: description_data[0].color
            });

            this.textGroup.push({
                tag: 1,
                outputTextGroup: outputTextGroup
            })
            this.$nextTick(() => {
                this.scrollToBottom();
            })
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
            // this.inputText = this.inputText.trim();
        },
        textGroup: {
            handler (newVal, oleVal) {
                // // console.log(this.textGroup.length);
                // setTimeout(() => {
                //     document.getElementById('group_' + (this.textGroup.length - 2)).style.opacity = 1;
                // }, 500);

                // setTimeout(() => {
                //     document.getElementById('group_' + (this.textGroup.length - 1)).style.opacity = 1;
                // }, 2000);
            },
            deep: true
        }
    },
    created () {
    },
    mounted () {
        this.inputText = "China's banks extended CNY 345.9 billion in new yuan loans in July 2023, the least since November of 2009 and well below market forecasts of CNY 800 billion. The value is also much lower than CNY 679 billion a year earlier and CNY 3.05 trillion in June, after a record CNY 15.73 trillion loans in the first half of the year. The reading adds to further evidence of a lacklustre economic recovery in China although July is usually a weak month for financing activities, with banks not in a rush to meet their lending targets at the beginning of the quarter."
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
