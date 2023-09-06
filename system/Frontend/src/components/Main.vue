<!--
 * @Description: 
 * @Author: Qing Shi
 * @Date: 2023-06-29 10:17:17
 * @LastEditors: Qing Shi
 * @LastEditTime: 2023-09-06 17:18:50
-->
<template>
    <div style="height: 100%; width: 100%;">
        <div style="font-family:KoHo; font-size: 22px; height: 40px; text-align: start; font-weight: bold;">
            <img src="../assets/img/3.png" width="25" alt="">&nbsp; Data Chart
            <hr>
        </div>
        <div style="height: calc(100% - 40px); width: 100%;">
            <div style="height: 0px;">
                <!-- <v-sheet class="d-flex flex-wrap" style="height: 60px; margin: 0px; width: 100%;">
                    <v-sheet class="flex-1-0" style="padding: 0px 8px 0px; width: 25%;">
                        <v-select v-model="chartValue" :items="chartType" chips label="Chart Type"></v-select>
                    </v-sheet>

                    <v-sheet class="flex-1-0" style="padding: 0px 8px 0px; width: 25%;">
                        <v-select v-model="highlightValue" :items="highlightType" chips label="Highlight"
                            multiple></v-select>
                    </v-sheet>
                    <v-sheet class="flex-1-0" style="padding: 0px 8px 0px; width: 25%;">
                        <v-select v-model="annotationValue" :items="annotationType" chips multiple
                            label="Annotation"></v-select>
                    </v-sheet>

                    <v-sheet class="flex-1-0" style="padding: 0px 8px 0px; width: 25%;">
                        <v-select v-model="otherValue" :items="othersType" multiple label="Others">
                            <template v-slot:selection="{ item, index }">
                                <v-chip v-if="index < 1" size="small">
                                    <span>{{ item.title }}</span>
                                </v-chip>
                                <span v-if="index === 1" class="text-grey text-caption align-self-center">
                                    (+{{ otherValue.length - 1 }} others)
                                </span>
                            </template>
                        </v-select>
                    </v-sheet>
                </v-sheet> -->
            </div>
            <div style="height: calc(70%); width: 100%;" v-loading="initChart" ref="mainView" id="mainView">
                <component :is="tabs[chartType[chartData['chartType']]]" :rawData="rawData" :chartData="chartData"
                    :defaultTag="1" :scaleTag="1" :stateTag="'state0'"></component>
            </div>
            <hr>
            <!-- display: flex; justify-content: space-between; align-items: center; -->
            <div
                style="height: calc(30% - 0px); width: 100%; background-color: white; display: flex; justify-content: space-between; align-items: center; overflow-y: auto;">
                <div
                    style="height: 95%; width: 33%; border-radius: 5px; border: 1.5px solid rgba(99, 99, 99, .6); align-items: center;display: flex; justify-content: center; margin: 3px;">
                    <div class="overlayTag" style="position: absolute; top: 10px; left: 30px;">Marker</div>
                    <div>
                        <div style="height:50px;"></div>
                        <component :is="tabs[chartType[chartData['chartType']]]" :rawData="rawData" :chartData="chartData"
                            :defaultTag="0" :scaleTag=".33" :stateTag="'state1'"></component>
                    </div>
                </div>
                <div
                    style="height: 95%; width: 33%; border-radius: 5px; border: 1.5px solid rgba(99, 99, 99, .6); align-items: center;display: flex; justify-content: center; margin: 3px;">
                    <div class="overlayTag" style="position: absolute; top: 10px; left: 30px;">Label</div>
                    <div>
                        <div style="height:50px;"></div>
                        <component :is="tabs[chartType[chartData['chartType']]]" :rawData="rawData" :chartData="chartData"
                            :defaultTag="0" :scaleTag=".33" :stateTag="'state2'"></component>
                    </div>
                </div>
                <div
                    style="height: 95%; width: 33%; border-radius: 5px; border: 1.5px solid rgba(99, 99, 99, .6); align-items: center;display: flex; justify-content: center; margin: 3px;">
                    <div class="overlayTag" style="position: absolute; top: 10px; left: 30px;">Highlight</div>
                    <div>
                        <div style="height:50px;"></div>
                        <component :is="tabs[chartType[chartData['chartType']]]" :rawData="rawData" :chartData="chartData"
                            :defaultTag="0" :scaleTag=".33" :stateTag="'state3'"></component>
                    </div>
                </div>
                <div
                    style="height: 95%; width: 33%; border-radius: 5px; border: 1.5px solid rgba(99, 99, 99, .6); align-items: center;display: flex; justify-content: center;">
                    <div class="overlayTag" style="position: absolute; top: 10px; left: 30px;">Marker</div>
                    <div>
                        <div style="height:50px;"></div>
                        <component :is="tabs[chartType[chartData['chartType']]]" :rawData="rawData" :chartData="chartData"
                            :defaultTag="0" :scaleTag=".33" :stateTag="'state3'"></component>
                    </div>
                </div>

            </div>
        </div>
    </div>
</template>
<script>
import { useDataStore } from "../stores/counter";
import singleBar from "./chart/singleBar.vue";
import singleLine from "./chart/singleLine.vue";
import multipleBar from "./chart/multipleBar.vue";
import multipleLine from "./chart/multipleLine.vue";
export default {
    name: "DataChart",
    props: [],
    data () {
        return {
            msg1: "Hello, main!",
            rawData: [],
            chartData: {},
            tabs: {
                'Single bar chart': 'singleBar',
                'Single line chart': 'singleLine',
                'Multiple bar chart': 'multipleBar',
                'Multiple line chart': 'multipleLine'
            },
            chartType: ['Single bar chart', 'Single line chart', 'Multiple bar chart', 'Multiple line chart'],
            chartValue: null,
            highlightType: ['Color', 'Area', 'Background'],
            highlightValue: [],
            annotationType: ['Marker', 'Label', 'Text'],
            annotationValue: [],
            othersType: ['Add Line (with Arrow)', 'Design Configuration'],
            otherValue: [],
            overlayTag: {
                highlight: {},
                annotation: {}
            },
            initChart: true
        };
    },
    methods: {
    },
    created () {
    },
    computed: {
        // initChart () {
        //     // console.log(this.chartData == null)
        //     return this.chartData == null;
        // }
    },
    mounted () {
        // console.log(chart_data)
        const dataStore = useDataStore()
        // console.log(dataStore.chart_data)

        dataStore.$subscribe(mutations => {
            // console.log(mutations);
            if (mutations.events.key == 'chart_data') {
                this.chartData = dataStore.chart_data;
                this.rawData = dataStore.data;
                this.initChart = false
                this.chartValue = this.chartData.chartType;
                console.log(this.tabs[this.chartType[this.chartData.chartType]]);
            }
        })
    },
    watch: {
        // highlightValue (newVal, oldVal) {
        //     this.overlayTag.highlight = {};
        //     const dataStore = useDataStore();
        //     for (let i in this.highlightValue) {
        //         this.overlayTag.highlight[this.highlightValue[i]] = 1;
        //     }
        //     dataStore.overlayTag = this.overlayTag;
        // },
        // annotationValue () {
        //     this.overlayTag.annotation = {};
        //     const dataStore = useDataStore();
        //     for (let i in this.annotationValue) {
        //         this.overlayTag.annotation[this.annotationValue[i]] = 1;
        //     }
        //     dataStore.overlayTag = this.overlayTag;
        // }
    },
    components: { singleBar, singleLine, multipleBar, multipleLine }
}
</script>
<style scoped>
.overlayTag {
    font-family: KoHo;
    background-color: rgb(99, 99, 99, .2);
    border-radius: 20px;
    padding: 3px 10px 3px 10px;
    font-weight: 600;
    font-style: italic;
}
</style>
