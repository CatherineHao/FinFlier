/*
 * @Description:
 * @Author: Qing Shi
 * @Date: 2022-09-17 23:36:36
 * @LastEditTime: 2023-02-02 15:02:39
 */
import {
    fetchBasicChart,
    fetchHello,
    postQuery,
    uploadData,
} from "../service/module/dataService";
// import {
//     ref,
//     computed
// } from "vue";
import { defineStore } from "pinia";

// export const useCounterStore = defineStore("counter", {
//   const count = ref(0);
//   const doubleCount = computed(() => count.value * 2);
//   function increment() {
//     count.value++;
//   }

//   return { count, doubleCount, increment };
// });

export const useDataStore = defineStore("dataStore", {
    state: () => {
        return {
            msg: "Hello, Vue SQ",
            data: [],
            chart_data: null,
            overlayTag: {
                highlight: {},
                annotation: {},
            },
            selectTable: null,
            objectTag: {},
            query_results: [],
            show_state: 0,
            state_map: {
                state0: {
                    overlay_tag: [],
                    chart_setting: {elWidth: 0,
                        elHeight: 0,
                        currentColor: {
                            r: 0,
                            g: 0,
                            b: 0,
                            a: 1
                        },
                        size: {
                            width: 100
                        },
                        axis: {
                            x: 'Position',
                            y: "Billions of dollars"
                        }},
                    overlay_setting: {
                        object0: {},
                        object1: {}
                    }
                }
            },
            type_chart_setting: {
                'Single bar chart': {
                    elWidth: 0,
                    elHeight: 0,
                    currentColor: {
                        r: 0,
                        g: 0,
                        b: 0,
                        a: 1
                    },
                    size: {
                        width: 100
                    },
                    axis: {
                        x: 'Position',
                        y: "Billions of dollars"
                    }
                },
                overlayFormat: {
                    color: {
                        currentColor: {
                            r: 0,
                            g: 0,
                            b: 0,
                            a: 1
                        }
                    },
                    'bounding box': {
                        currentColor: {
                            r: 0,
                            g: 0,
                            b: 0,
                            a: 1
                        }
                    },
                    background: {
                        currentColor: {
                            r: 0,
                            g: 0,
                            b: 0,
                            a: 1
                        }
                    },
                    marker: {
                        currentColor: {
                            r: 0,
                            g: 0,
                            b: 0,
                            a: 1
                        }
                    },
                    label: {
                        currentColor: {
                            r: 0,
                            g: 0,
                            b: 0,
                            a: 1
                        }
                    },
                    text: {
                        currentColor: {
                            r: 0,
                            g: 0,
                            b: 0,
                            a: 1
                        }
                    },
                    
                }
            },
            default_setting: {
                chart_setting: {
                },
                overlay_setting: {

                }
            }
        };
    },
    actions: {
        fetchHello () {
            const st = new Date();
            fetchHello({}, (resp) => {
                this.msg = resp;
                console.log("Fetch Hello Time: ", st - new Date());
            });
        },
        uploadData (param) {
            const st = new Date();
            uploadData(param, (resp) => {
                this.profileData = resp;
                console.log("Uploading File: ", new Date() - st);
            });
        },
        fetchBasicChart (param) {
            const st = new Date();
            fetchBasicChart(param, (resp) => {
                // setTimeout(() => {
                this.chart_data = resp.data;
                // }, 3000);
                console.log("Fetch Data: ", new Date() - st);
            });
        },
        postQuery (param) {
            const st = new Date();
            postQuery(param, (resp) => {
                // setTimeout(() => {
                this.query_results.push(resp.data);
                // }, 1000);
                console.log("Post Query: ", new Date() - st);
            })
        }
    },
});
