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
            changeTag: 0,
            timeChange: 0,
            calcOverlayTag: 0,
            overallData: [],
            positionData: {},
            startPositionData: {},
            chart_data: null,
            narrative_num: 0,
            overlayTag: {
                highlight: {},
                annotation: {},
            },
            selectTable: null,
            graphicalOverlayData: null,
            objectTag: {},
            selectObject: '',
            query_results: [],
            show_state: 0,
            objectCnt: 0,
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
                    }
                },
                state1: {
                    overlay_tag: [0, 0, 0, 1, 0, 0, 0, 0, 0],
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
                    }
                },
                state2: {
                    overlay_tag: [0, 1, 0, 0, 0, 0, 0, 0, 0],
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
                    }
                },
                state3: {
                    overlay_tag: [0, 0, 1, 0, 0, 0, 0, 0, 0],
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
                            r: 208,
                            g: 211,
                            b: 199,
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
                            r: 220,
                            g: 220,
                            b: 220,
                            a: 1
                        }
                    },
                    marker: {
                        currentColor: {
                            r: 255,
                            g: 0,
                            b: 0,
                            a: 1
                        }
                    },
                    label: {
                        currentColor: {
                            r: 255,
                            g: 0,
                            b: 0,
                            a: 1
                        }
                    },
                    text: {
                        currentColor: {
                            r: 255,
                            g: 0,
                            b: 0,
                            a: 1
                        }
                    },
                    
                    trend: {
                        currentColor: {
                            r: 255,
                            g: 0,
                            b: 0,
                            a: 1
                        }
                    },
                    overall: {
                        currentColor: {
                            r: 255,
                            g: 0,
                            b: 0,
                            a: 1
                        }
                    },
                    special: {
                        currentColor: {
                            r: 255,
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
                // for (let i in this.query_results[this.query_results.length - 1].final) {
                //     this.query_results[this.query_results.length - 1].final[i]['ObjectName'] = 'object' + (this.objectCnt).toString();
                //     this.query_results[this.query_results.length - 1].final[i]['ObjectIndex'] = (this.objectCnt);
                //     this.query_results[this.query_results.length - 1].final[i]['ObjectIndex'] = ;
                //     this.objectCnt++;
                // }
                // console.log(this.query_results);

                // }, 1000);
                console.log("Post Query: ", new Date() - st);
            })
        }
    },
});
