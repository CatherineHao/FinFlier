<!--
 * @Description: 
 * @Author: Qing Shi
 * @Date: 2023-06-29 10:17:17
 * @LastEditors: Qing Shi
 * @LastEditTime: 2023-07-14 10:45:24
-->
<template>
    <div style="height: 100%; width: 100%;">
        <div style="font-family:KoHo; font-size: 22px; height: 40px; text-align: start; font-weight: bold;">
            Data Chart
            <hr>
        </div>
        <div style="height: calc(100% - 40px); width: 100%;">
            <div style="height: 60px;">
                <v-sheet class="d-flex flex-wrap" style="height: 60px; margin: 0px; width: 100%;">
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
                </v-sheet>
                <!-- <v-sheet class="d-flex flex-wrap" style="height: 60px; margin: 0px; width: 100%;">
                    <v-sheet class="flex-1-0" style="padding: 0px 8px 0px; width: 50%;">
                        <v-select v-model="annotationValue" :items="annotationType" chips multiple
                            label="Annotation"></v-select>
                    </v-sheet>

                    <v-sheet class="flex-1-0" style="padding: 0px 8px 0px; width: 50%;">
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
            <div style="height: calc(100% - 60px); width: 100%;" v-loading="initChart">
                <component :is="tabs[chartData['chartType']]" :rawData="rawData" :chartData="chartData"></component>
            </div>
        </div>
    </div>
</template>
<script>
import { useDataStore } from "../stores/counter";
import singleBar from "./chart/singleBar.vue";
import chart_data from "../assets/data/chart.json";
export default {
    name: "DataChart",
    props: [],
    data () {
        return {
            msg1: "Hello, main!",
            rawData: [],
            chartData: {},
            tabs: {
                'Single bar chart': 'singleBar'
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
            }
        })
    },
    watch: {
        highlightValue (newVal, oldVal) {
            this.overlayTag.highlight = {};
            const dataStore = useDataStore();
            for (let i in this.highlightValue) {
                this.overlayTag.highlight[this.highlightValue[i]] = 1;
            }
            dataStore.overlayTag = this.overlayTag;
        },
        annotationValue () {
            this.overlayTag.annotation = {};
            const dataStore = useDataStore();
            for (let i in this.annotationValue) {
                this.overlayTag.annotation[this.annotationValue[i]] = 1;
            }
            dataStore.overlayTag = this.overlayTag;
        }
    },
    components: { singleBar }
}
</script>
<style scoped></style>
