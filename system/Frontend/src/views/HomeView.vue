<!--
 * @Description: 
 * @Author: Qing Shi
 * @Date: 2023-06-29 10:17:17
 * @LastEditors: Qing Shi
 * @LastEditTime: 2023-08-22 14:36:13
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
<template>
    <!-- bg-surface-variant -->
    <!-- <v-container class="bg-surface-variant" style="min-height: calc(100vh - 0px); width: 100%; margin-right: 0px; margin-left: 0px;" > -->
    <!-- <v-row>
            <div 
                style="width: 100%;height: 50px;text-align: start;font-family: 'operator Mono Lig'; font-style: italic; font-size: 30px;margin-bottom: 10px; padding-left: 20px;">
                FinTeller</div>
        </v-row> -->
    <div
        style="width: 100%; height: 50px;text-align: start;font-family: 'operator Mono Lig'; font-style: italic; font-size: 30px;margin-bottom: 0px; padding-left: 20px; display: flex;">
        <div style="margin-top: 5px;">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" height="30" width="30" fill="rgba(0, 0, 0, 0.7)">
                <path d="M0 0h24v24H0z" fill="none" />
                <path d="M19 4h-4L7.11 16.63 4.5 12 9 4H5L.5 12 5 20h4l7.89-12.63L19.5 12 15 20h4l4.5-8z" />
            </svg>
        </div>
        <div style="margin-left: 10px">FinTeller</div>
    </div>
    <div style="height: calc(100vh - 50px ); width: 100%; display: flex;">
        <div style="height: calc((100% - 10px) / 2); width: calc(20% - 10px); margin-left: 10px; margin-bottom: 10px; padding: 8px; position: absolute; top: 0px;"
            class="boundary">
            <DataTable />
        </div>

        <div style="height: calc((100% - 10px) / 2 - 10px); width: calc(20% - 10px); margin-left: 10px; margin-bottom: 10px; padding: 8px; position: absolute; bottom: 0px;"
            class="boundary">
            <DataDescription />
        </div>
        <div style="height: calc(100% - 10px); width: calc(60% - 10px); margin-left: 10px; margin-bottom: 10px; padding: 8px; position: absolute; left: calc(20% - 0px);"
            class="boundary">
            <Main />
        </div>
        <div style="height: calc(100% - 10px); width: calc(20% - 20px); margin-left: 10px; margin-bottom: 10px; padding: 8px; position: absolute; right: 10px;"
            class="boundary">
            <DesignPanel />
        </div>
    </div>
</template>

<script>
import Main from '../components/Main.vue';
import { useDataStore } from "../stores/counter";
import DataTable from '../components/DataTable.vue';
import DataDescription from '../components/DataDescription.vue';
import DesignPanel from '../components/DesignPanel.vue';

export default {
    name: "home_view",
    data () {
        return {
            msgH: null,
            rawData: []
        };
    },
    computed: {
        initSign () {
            return 1;
        },
        loadingText () {
            return "Loading"
        }
    },
    mounted () {
        this.msgH = 1;
        const dataStore = useDataStore();
    },
    methods: {
        fetchData () { }
    },
    components: { Main, DataTable, Main, DataDescription, DesignPanel }
};
</script>

<style scoped>
.boundary {
    /*border-style: dashed;*/
    border-style: solid;
    border-color: #d3dce6;
    border-width: 0.5px;
    border-radius: 3px;
    box-shadow: 1px 2px 3px 1px #bdbaba;
}
</style>
