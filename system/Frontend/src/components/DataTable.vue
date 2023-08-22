<template>
    <div>
        <div style="font-family: KoHo, 'operator Mono Lig'; font-size: 22px;  height: 40px; text-align: start; font-weight: bold;">
            Data Table
            <hr>
        </div>
        <v-expand-transition>
            <div v-show="expand" style="overflow-y: auto; overflow-x: auto;">
                <table style="border-collapse:separate; border-spacing:0px 5px; width: 100%">
                    <thead style="height: 30px; border-radius: 10px;">
                        <tr style="border-radius: 0px; 
    box-shadow: 0px 1px 1px 0px #bdbaba;">
                            <th style="text-align: center; width: 30px;">
                                id
                            </th>
                            <th v-for="(item, i) in th" :key="'th' + i" style="text-align: center;">
                                {{ item }}
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <!-- #ddeff6 -->
                        <tr v-for="(item, i) in td" :key="'td' + i" class="td_tr" style="height: 30px;">
                            <td :style="{
                                'text-align': 'center',
                                'border-top-left-radius': '5px',
                                'border-bottom-left-radius': '5px',
                                'transition': '0.4s'
                            }" :id="'cellR' + i + 'C' + '0'" :ref="'cellR' + i + 'C' + '0'">
                                {{ i }}
                            </td>
                            <td v-for="(o, oi) in th" :key="'td_' + oi" :id="'cellR' + i + 'C' + (oi + 1)" :ref="'cellR' + i + 'C' + (oi + 1)" :style="{
                                'text-align': 'center',
                                'border-top-right-radius': oi == (th.length - 1) ? '5px' : '0px',
                                'border-bottom-right-radius': oi == (th.length - 1) ? '5px' : '0px',
                                'transition': '0.4s'
                            }">
                                {{ item[o] }}
                            </td>
                        </tr>
                    </tbody>
                </table>
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
            msg1: "Hello, main!",
            rawData: [],
            th: [],
            td: [],
            tableTag: {},
            expand: false
        };
    },
    methods: {
        calcTable (data) {
            let th = data.columns;
            return [th, data];
        }
    },
    created () {
    },
    computed: {
    },
    mounted () {
        const dataStore = useDataStore();
        this.rawData = dataStore.data;
        [this.th, this.td] = this.calcTable(this.rawData);
        // console.log(this.rawData)
        setTimeout(() => this.expand = !this.expand, 100);
        dataStore.$subscribe(() => {
            this.tableTag = dataStore.selectTable;
            // console.log(this.tableTag);
            for (let i in this.tableTag) {
                // console.log(this.);
                const element = document.getElementById(i);
                    // console.log(element.style);
                if (this.tableTag[i].tag == 1) {
                    element.style.backgroundColor = this.tableTag[i].color;
                } else {
                    element.style.backgroundColor = 'white';
                }
            }
            // console.log(this.tableTag, dataStore.selectTable)
        })
    },
    components: {}
}
</script>
<style scoped>
table {
    /* border-collapse:collapse; */
}

/* td {
    border: 1px solid black;
} */
.td_tr {
    border-radius: 8px;
    box-shadow: 0px 2px 3px 1px #bdbaba;
}

td {
    /* border-radius: 5px; */
    /* background-color: aquamarine; */
}
</style>
