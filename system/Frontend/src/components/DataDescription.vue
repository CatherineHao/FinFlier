<!--
 * @Description: 
 * @Author: Qing Shi
 * @Date: 2023-08-22 14:28:15
 * @LastEditors: Qing Shi
 * @LastEditTime: 2023-09-06 18:19:09
-->
<!--
 *                        _oo0oo_
 *                       o8888888o
 *                       88" . "88
 *                       (| -_- |)
 *                       0\  =  /0
 *                     ___/`---'\___
 *                   .' \\|     |// '.
 *                  / \\|||  :  |||// \
 *                 / _||||| -:- |||||- \
 *                |   | \\\  - /// |   |
 *                | \_|  ''\---/''  |_/ |
 *                \  .-\__  '-'  ___/-. /
 *              ___'. .'  /--.--\  `. .'___
 *           ."" '<  `.___\_<|>_/___.' >' "".
 *          | | :  `- \`.;`\ _ /`;.`/ - ` : | |
 *          \  \ `_.   \_ __\ /__ _/   .-` /  /
 *      =====`-.____`.___ \_____/___.-`___.-'=====
 *                        `=---='
 * 
 * 
 *      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 * 
 *            佛祖保佑     永不宕机     永无BUG
 -->

<!--
 * @Description: 
 * @Author: Qing Shi
 * @Date: 2023-07-10 18:18:22
 * @LastEditors: Qing Shi
 * @LastEditTime: 2023-08-29 00:14:11
-->
<template>
    <div style="height: 100%; width: 100%;">
        <div style="font-family: KoHo; text-align: start; font-size: 22px;height: 40px; font-weight: bold;">

            <img src="../assets/img/2.png" width="25" alt=""> &nbsp;Conversation Panel
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
                        <div v-if="item.tag == 1" style=" width: 40px; padding-top: 3px; padding-left: 0px;">
                            <div
                                style="background-color: rgb(91, 155, 255); width: 35px; height: 35px; border-radius: 6px; padding: 4px;">

                                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="#FFF">
                                    <path d="M0 0h24v24H0z" fill="none" />
                                    <path
                                        d="M19 4h-4L7.11 16.63 4.5 12 9 4H5L.5 12 5 20h4l7.89-12.63L19.5 12 15 20h4l4.5-8z" />
                                </svg>

                            </div>
                        </div>
                        <div style="width: calc(100% - 40px);">
                            <div v-if="item.tag == -1"
                                style="width: 100%; line-height:1lh; text-align: start; padding-right: 5px; background-color: rgb(173, 216, 230, 0); padding: 8px; border-radius: 5px; border: 1px solid rgba(0, 0, 0, .3);">
                                <!-- <div style="width: 95%;">{{ item.text }}</div> -->
                                <div style="width: 100%;display: flex;justify-content: flex-end;">
                                    <svg t="1693450336410" class="icon" viewBox="0 0 1024 1024" version="1.1"
                                    xmlns="http://www.w3.org/2000/svg" p-id="4007" width="20" height="20">
                                    <path
                                        d="M853.333333 501.333333c-17.066667 0-32 14.933333-32 32v320c0 6.4-4.266667 10.666667-10.666666 10.666667H170.666667c-6.4 0-10.666667-4.266667-10.666667-10.666667V213.333333c0-6.4 4.266667-10.666667 10.666667-10.666666h320c17.066667 0 32-14.933333 32-32s-14.933333-32-32-32H170.666667c-40.533333 0-74.666667 34.133333-74.666667 74.666666v640c0 40.533333 34.133333 74.666667 74.666667 74.666667h640c40.533333 0 74.666667-34.133333 74.666666-74.666667V533.333333c0-17.066667-14.933333-32-32-32z"
                                        fill="#666666" p-id="4008"></path>
                                    <path
                                        d="M405.333333 484.266667l-32 125.866666c-2.133333 10.666667 0 23.466667 8.533334 29.866667 6.4 6.4 14.933333 8.533333 23.466666 8.533333h8.533334l125.866666-32c6.4-2.133333 10.666667-4.266667 14.933334-8.533333l300.8-300.8c38.4-38.4 38.4-102.4 0-140.8-38.4-38.4-102.4-38.4-140.8 0L413.866667 469.333333c-4.266667 4.266667-6.4 8.533333-8.533334 14.933334z m59.733334 23.466666L761.6 213.333333c12.8-12.8 36.266667-12.8 49.066667 0 12.8 12.8 12.8 36.266667 0 49.066667L516.266667 558.933333l-66.133334 17.066667 14.933334-68.266667z"
                                        fill="#666666" p-id="4009"></path>
                                </svg>
                                &nbsp;
                                <svg t="1693453733613" class="icon" viewBox="0 0 1024 1024" version="1.1"
                                    xmlns="http://www.w3.org/2000/svg" p-id="8200" width="20" height="20">
                                    <path
                                        d="M512 832c-176.448 0-320-143.552-320-320S335.552 192 512 192s320 143.552 320 320-143.552 320-320 320m0-704C300.256 128 128 300.256 128 512s172.256 384 384 384 384-172.256 384-384S723.744 128 512 128"
                                        fill="#3E3A39" p-id="8201"></path>
                                    <path
                                        d="M649.824 361.376a31.968 31.968 0 0 0-45.248 0L505.6 460.352l-98.976-98.976a31.968 31.968 0 1 0-45.248 45.248l98.976 98.976-98.976 98.976a32 32 0 0 0 45.248 45.248l98.976-98.976 98.976 98.976a31.904 31.904 0 0 0 45.248 0 31.968 31.968 0 0 0 0-45.248L550.848 505.6l98.976-98.976a31.968 31.968 0 0 0 0-45.248"
                                        fill="#3E3A39" p-id="8202"></path>
                                </svg>
                                </div>
                                <div>{{ item.text }}</div>
                                
                            </div>
                            <div v-else v-loading="item.loading"
                                style="width: 100%; line-height:1lh; text-align: start; padding: 8px; background-color: rgb(173, 216, 230, 0); border-radius:5px; min-height: 40px; border: 1px solid rgba(0, 0, 0, .3);">
                                <div>

                                <svg t="1693451515962" class="icon" viewBox="0 0 1024 1024" version="1.1"
                                    xmlns="http://www.w3.org/2000/svg" p-id="6791" width="15" height="15">
                                    <path
                                        d="M796.444672 56.889344c37.925888 0 56.88832 18.962432 56.88832 56.88832V512c0 56.889344-199.110656 28.444672-227.555328 85.332992-28.444672 56.889344 0 199.11168 0 227.556352 0 28.443648 0 142.221312-113.777664 142.221312s-113.777664-113.77664-113.777664-142.221312c0-28.444672 28.444672-170.667008 0-227.556352C369.77664 540.444672 170.667008 568.889344 170.667008 512V113.777664c0-37.925888 18.962432-56.88832 56.88832-56.88832h568.889344z m0 227.555328H227.555328v204.99456c10.979328 2.740224 26.42944 5.195776 53.741568 8.83712 6.15424 0.8192 6.15424 0.8192 12.4416 1.664 93.700096 12.649472 131.45088 24.12032 155.3664 71.95136 16.590848 33.181696 20.67968 76.36992 17.878016 132.754432-1.041408 20.963328-2.996224 42.380288-5.925888 67.76832-0.986112 8.546304-4.00896 33.332224-4.355072 36.296704-1.08544 9.288704-1.591296 14.892032-1.591296 16.178176 0 57.38496 12.422144 85.332992 56.889344 85.332992 30.396416 0 42.82368-10.43968 50.661376-34.823168 4.840448-15.059968 6.227968-29.889536 6.227968-50.509824 0-1.286144-0.505856-6.889472-1.591296-16.178176-0.346112-2.96448-3.36896-27.7504-4.355072-36.297728-2.92864-25.387008-4.88448-46.803968-5.925888-67.767296-2.801664-56.384512 1.287168-99.572736 17.878016-132.754432 23.91552-47.83104 61.666304-59.301888 155.3664-71.95136 6.28736-0.8448 6.28736-0.8448 12.4416-1.664 27.311104-3.641344 42.76224-6.096896 53.741568-8.83712v-204.99456z m0-170.667008H227.555328v113.777664h568.889344v-113.77664z"
                                        fill="#323233" p-id="6792"></path>
                                </svg>
                                &nbsp;
                                <svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24"
                                    stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="15" width="15"
                                    xmlns="http://www.w3.org/2000/svg">
                                    <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2">
                                    </path>
                                    <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
                                </svg>
                                &nbsp;
                                <svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24"
                                    stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="15" width="15"
                                    xmlns="http://www.w3.org/2000/svg">
                                    <path
                                        d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3">
                                    </path>
                                </svg>
                                &nbsp;
                                <svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24"
                                    stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="15" width="15"
                                    xmlns="http://www.w3.org/2000/svg">
                                    <path
                                        d="M10 15v4a3 3 0 0 0 3 3l4-9V2H5.72a2 2 0 0 0-2 1.7l-1.38 9a2 2 0 0 0 2 2.3zm7-13h2.67A2.31 2.31 0 0 1 22 4v7a2.31 2.31 0 0 1-2.33 2H17">
                                    </path>
                                </svg>
                                </div>
                                <div>
                                <span v-for="(o, i) in item.outputTextGroup" :key="'res_' + i"
                                    :class="{ 'dataObject': o.tag != -1 }" :id="o.id" :style="{
                                        backgroundColor: o.tag == 0 || o.tag == 2 ? o.back_color : 'white',
                                        'border-bottom': o.tag == 2 || o.tag == 1 ? '3px solid ' + o.color : '0px',
                                        'text-decoration-color': o.color
                                    }" @click="o.tag != -1 ? hoverObject(o) : ''"
                                    @mouseenter="o.tag != -1 ? handleHover(o) : ''"
                                    @mouseout="o.tag != -1 ? handleOut(o) : ''">{{ o.text }}</span>
                                <!-- <br>
                                <br> -->
                                <div v-if="item.loading != 1 && item_i == 1">
                                <hr style="margin-top: 10px; margin-bottom: 5px;">
                                    <div style="font-weight: 600;">
                                        Reason:</div>
                                    <div>
                                        {{ item.reason }}
                                    </div>
                                </div></div>
                            </div>
                        </div>

                        <div v-if="item.tag == -1" style="padding-top: 3px; padding-left: 0px; width: 40px;">
                            <div
                                style="background-color: rgb(91, 155, 255); width: 35px; height: 35px; border-radius: 6px; padding: 4px; float: right;">

                                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="#FFF">
                                    <path d="M0 0h24v24H0z" fill="none" />
                                    <path
                                        d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z" />
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
import { selectAll } from "d3";
import { useDataStore } from "../stores/counter";
// import description_data from "@/assets/data/test.json"
export default {
    name: "DataTable",
    props: [],
    data () {
        return {
            inputText: '',
            outputText: '',
            firstInput: '',
            outputTextArray: [],
            textGroup: [],
            objectTag: {},
            postTag: 0,
            objectCnt: 0,
            store_data: [],
            query_len: 0,
            color_map: [{
                "r": 174, "g": 205, "b": 234, "a": 1
            }, {
                "r": 196, "g": 223, "b": 155, "a": 1
            }, {
                "r": 250, "g": 243, "b": 210, "a": 1
            },
            {
                "r": 249, "g": 203, "b": 220, "a": 1
            }],
        };
    },
    methods: {
        colorTrans (color) {
            return `rgba(${color.r}, ${color.g}, ${color.b}, ${color.a})`
        },
        scrollToBottom () {
            this.$refs.scrollableDiv.scrollTop = this.$refs.scrollableDiv.scrollHeight;
        },
        handleHover (o) {
            selectAll("#" + o.id).style('border-top-color', 'black');
            selectAll("#" + o.id).style('border-left-color', 'black');
            selectAll("#" + o.id).style('border-right-color', 'black');
        },
        handleOut (o) {

            selectAll("#" + o.id).style('border-top-color', 'white');
            selectAll("#" + o.id).style('border-left-color', 'white');
            selectAll("#" + o.id).style('border-right-color', 'white');
        },
        submitText () {
            const dataStore = useDataStore();
            let rawData = dataStore.data;
            this.inputText = this.inputText.trim();
            this.textGroup.push({
                tag: -1,
                text: this.inputText
            })
            this.$nextTick(() => {
                this.scrollToBottom();
            })
            let inputText = this.inputText;
            this.inputText = "";
            let user_info = '';
            let postTag = 'following';
            if (this.postTag == 0) {
                postTag = 'start'
                this.firstInput = inputText;
                this.postTag = 1;
            }
            for (let i = 0; i < rawData.length; ++i) {
                for (let j in rawData[i]) {
                    // console.log(j)
                    if (!isNaN(rawData[i][j])) {
                        rawData[i][j] = parseFloat(rawData[i][j]);
                    }
                }
                // break
            }
            function stringifyArray (arr) {
                // 递归函数，用于处理数组和对象
                function stringify (obj) {
                    if (typeof obj === 'object' && obj !== null) {
                        if (Array.isArray(obj)) {
                            // 处理数组
                            const resultArray = obj.map(item => stringify(item));
                            return `[${resultArray.join(',')}]`;
                        } else {
                            // 处理对象
                            const resultObject = Object.keys(obj).map(key => {
                                const value = obj[key];
                                return `"${key}":${stringify(value)}`;
                            });
                            return `{${resultObject.join(',')}}`;
                        }
                    } else if (typeof obj === 'string') {
                        return `"${obj}"`;
                    } else {
                        // 对于数字等其他类型，保持不变
                        return String(obj);
                    }
                }

                return stringify(arr);
            }
            this.textGroup.push({
                tag: 1,
                outputTextGroup: {},
                reason: '',
                loading: 1
            })
            // console.log(rawData[0], stringifyArray([rawData[0]]))
            if (postTag == 'start') {
                user_info = 'data: ' + stringifyArray(rawData) + 'text: ["' + inputText + '"]label: "' + postTag + '"';
            } else {
                user_info = 'data: ' + stringifyArray(rawData) + 'text: ["' + this.firstInput + '"]' + dataStore.query_results[0].result + dataStore.query_results[0].reason + 'question: ["' + inputText + '"]label: "' + postTag + '"';
                // console.log(user_info);
            }
            // console.log(user_info);
            // if (postTag == 'start')
            dataStore.postQuery({
                data: user_info,
                label: postTag
            })
            // console.log(dataStore.query_results)
            // console.log(description_data);
        },
        gptFeedback (description_data, reason_data) {
            // console.log(reason_data)
            // console.log(description_data)
            for (let i in description_data) {
                description_data[i]['ObjectName'] = 'object' + this.objectCnt.toString();
                description_data[i]['ObjectIndex'] = this.objectCnt;
                description_data[i]['color'] = this.color_map[this.objectCnt]
                this.objectCnt++;
            }

            // console.log(description_data)
            let originalText = description_data[0]['OriginText'];
            // console.log(originalText);
            let outputTextGroup = [];
            let startPos = 0;
            let endPos = 0;
            // const dataStore = useDataStore();
            // let overlay_set = d
            const dataStore = useDataStore();
            dataStore.graphicalOverlayData = description_data;
            for (let i in description_data) {
                // console.log(description_data[i]['ObjectName'])
                let tmp = {}, tmp1 = {}, tmp2 = {}, tmp3 = {};
                tmp['overlay_tag'] = [0, 0, 0, 0, 0, 0, 0, 0, 0];
                tmp1['overlay_tag'] = [0, 0, 0, 1, 0, 0, 0, 0, 0];
                tmp2['overlay_tag'] = [0, 0, 0, 0, 1, 0, 0, 0, 0];
                tmp3['overlay_tag'] = [1, 0, 0, 0, 0, , 0, 0, 0];
                for (let j in dataStore.type_chart_setting.overlayFormat) {
                    tmp[j] = {};
                    tmp1[j] = {};
                    tmp2[j] = {};
                    tmp3[j] = {};
                    
                    for (let k in dataStore.type_chart_setting.overlayFormat[j]) {
                        tmp[j][k] = dataStore.type_chart_setting.overlayFormat[j][k];
                        tmp1[j][k] = dataStore.type_chart_setting.overlayFormat[j][k];
                        tmp2[j][k] = dataStore.type_chart_setting.overlayFormat[j][k];
                        tmp3[j][k] = dataStore.type_chart_setting.overlayFormat[j][k];
                    }
                }
                // for (let j in tmp) {
                //     tmp[j].currentColor = description_data[i]['color'];
                // }
                dataStore.state_map.state0.overlay_setting[description_data[i]['ObjectName']] = tmp;
                dataStore.state_map.state1.overlay_setting[description_data[i]['ObjectName']] = tmp1;
                dataStore.state_map.state2.overlay_setting[description_data[i]['ObjectName']] = tmp2;
                dataStore.state_map.state3.overlay_setting[description_data[i]['ObjectName']] = tmp3;
                // console.log(description_data[i]['ObjectName'], description_data[i]['color'], tmp)
            }
            // console.log(dataStore.state_map.state0.overlay_setting)
            // for (let i in )
            for (let i in description_data) {
                let pos = []
                for (let j in description_data[i].ConversationInfo) {
                    let info = description_data[i].ConversationInfo[j];
                    if (info.Position == null) continue;
                    if (typeof (info.Position[0]) == 'object') {
                        for (let k in info.Position) {
                            pos.push({
                                pos: info.Position[k],
                                tag: info.OverTag
                            })
                        }
                    } else {
                        pos.push({
                            pos: info.Position,
                            tag: info.OverTag
                        })
                    }
                    // console.log(pos)

                }
                pos.sort((a, b) => a.pos[0] - b.pos[0])
                for (let k in pos) {
                    endPos = pos[k].pos[0];
                    let s = originalText.slice(startPos, endPos);
                    if (startPos != endPos) {
                        // console.log(s)
                        outputTextGroup.push({
                            text: s,
                            tag: -1,
                        })
                    }
                    startPos = pos[k].pos[0];
                    endPos = pos[k].pos[1] + 1;
                    s = originalText.slice(startPos, endPos);
                    let bak_color = {}
                    for (let j in description_data[i].color)
                        bak_color[j] = description_data[i].color[j];
                    bak_color['a'] = 0.4
                    // console.log(description_data[i].color)
                    outputTextGroup.push({
                        id: description_data[i]['ObjectName'],
                        objectName: description_data[i]['ObjectName'],
                        text: s,
                        tag: pos[k].tag,
                        position: description_data[i]['Position'],
                        rawColor: description_data[i].color,
                        color: this.colorTrans(description_data[i].color),
                        back_color: this.colorTrans(bak_color)
                    });

                    startPos = endPos;
                }
            }
            // outputTextGroup.push({
            //     tag: 
            // })



            outputTextGroup.push({
                text: originalText.slice(startPos, originalText.length
                ),
                tag: -1
            });
            this.textGroup[this.textGroup.length - 1] = {
                tag: 1,
                loading: 0,
                outputTextGroup: outputTextGroup,
                reason: reason_data.slice(7, reason_data.length)
            }
            // console.log(this.textGroup)
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
            let rawData = dataStore.data;
            let th = rawData.columns;
            let t_cnt = [];
            for (let j in o.position) {
                let tt_cnt = 0;
                for (let i in th) {
                    if (th[i] == o.position[j]['Begin'][0]) {
                        break;
                    } else {
                        tt_cnt++;
                    }
                }
                t_cnt.push(tt_cnt);
            }
            let tableTag = {};
            // console.log(t_cnt)
            for (let j in t_cnt) {
                for (let i = parseInt(o.position[j]['Begin'][1]); i <= parseInt(o.position[j]['End'][1]); ++i) {
                    // console.log(o.color)
                    tableTag['cellR' + (i).toString() + 'C' + (t_cnt[j] + 1).toString()] = {
                        tag: 1,
                        color: o.color
                    };
                }
            }
            // console.log(tableTag);
            dataStore.selectTable = tableTag;
            console.log(tableTag)
            this.tableTag = tableTag;
            objectTag[o.objectName] = 1;
            dataStore.selectObject = o.objectName;
            dataStore.objectTag = objectTag;
            this.objectTag = objectTag;

            // let tmp = dataStore.type_chart_setting.overlayFormat;

            // for (let i in tmp) {
            //     tmp[i].currentColor = o.rawColor;
            // }
            // // console.log(dataStore.state_map['stage0']['overlay_setting'], o.objectName);


            // dataStore.state_map['state0']['overlay_setting'][o.objectName] = tmp;
            // console.log(dataStore.state_map['state0']['overlay_setting']);
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
            dataStore.selectObject = -1
        }
    },
    watch: {
        store_data: {
            handler (newVal) {
                // if (type)
                console.log(newVal);
                this.gptFeedback(newVal.final);
            },
            deep: true
        },
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
        // this.inputText = "Investment by British investors accounted for 18 percent of new foreign direct investment expenditures. The Netherlands ($43.1 billion) was the second-largest investing country, followed by France ($35.3 billion)."
        // this.inputText = "There exists a 'head and shoulder' pattern on the Amazon stock moving averages from 1999/09/27 to 2000/02/22.";
        // this.inputText = "The 12-month percentage change in Consumer Price Index for all items increased 4.9 percentage in 2023 April. Consumer Price Index for food rose 7.7 percent in the same month, while consumer prices for energy fell 5.1 percentage.";
        // this.inputText = "In 2023, the sales proportion of NEVs that were subcompact and below declined to 30%, from 61% in 2017. During the same periods of comparison, the mix of compact and midsize-to-large NEVs increased to 70% from 39%, reflecting the upgrade trend in terms of vehicle size.";
        // this.submitText();
        const dataStore = useDataStore();
        dataStore.$subscribe((mutations, state) => {
            console.log(mutations.type)
            if (this.query_len < state.query_results.length) {
                let info_data = state.query_results[state.query_results.length - 1];
                this.query_len = state.query_results.length;
                // // console.log(info_data);
                if (typeof (info_data) != 'undefined')
                    this.gptFeedback(info_data.final, info_data.reason);
                // console.log(info_data.reason)
            }
        })
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
    /* border-color: bal; */
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
