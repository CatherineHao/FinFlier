<!--
 * @Description: 
 * @Author: Qing Shi
 * @Date: 2023-06-29 10:17:17
 * @LastEditors: Qing Shi
 * @LastEditTime: 2023-08-28 21:38:03
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
                style="width: 100%;height: 50px;text-align: start;font-family: KoHo; font-style: italic; font-size: 30px;margin-bottom: 10px; padding-left: 20px;">
                FinTeller</div>
        </v-row> -->
    <div
        style="width: 100%; height: 45px;text-align: start;font-family: KoHo; font-style: italic; font-size: 30px;margin-bottom: 0px; padding-left: 20px; background-color: #404040;">
        <div style="margin-top: 0px; float: left;">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" height="30" width="30" fill="rgba(255, 255, 255, 1)">
                <path d="M0 0h24v24H0z" fill="none" />
                <path d="M19 4h-4L7.11 16.63 4.5 12 9 4H5L.5 12 5 20h4l7.89-12.63L19.5 12 15 20h4l4.5-8z" />
            </svg>
            <span style="margin-left: 10px; color: white; font-weight: 600;">FinCues</span>
        </div>
        <div style="float: right; margin-right: 10px; margin-top: -5px;">
            <el-button round><svg t="1693229871966" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="4839" width="20" height="20"><path d="M505.7 661c3.2 4.1 9.4 4.1 12.6 0l112-141.7c4.1-5.2 0.4-12.9-6.3-12.9h-74.1V168c0-4.4-3.6-8-8-8h-60c-4.4 0-8 3.6-8 8v338.3H400c-6.7 0-10.4 7.7-6.3 12.9l112 141.8z" p-id="4840"></path><path d="M878 626h-60c-4.4 0-8 3.6-8 8v154H214V634c0-4.4-3.6-8-8-8h-60c-4.4 0-8 3.6-8 8v198c0 17.7 14.3 32 32 32h684c17.7 0 32-14.3 32-32V634c0-4.4-3.6-8-8-8z" p-id="4841"></path></svg>&nbsp;Input</el-button>
            <el-button round><svg t="1693229895052" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="5815" width="20" height="20"><path d="M400 317.7h73.9V656c0 4.4 3.6 8 8 8h60c4.4 0 8-3.6 8-8V317.7H624c6.7 0 10.4-7.7 6.3-12.9L518.3 163c-3.2-4.1-9.4-4.1-12.6 0l-112 141.7c-4.1 5.3-0.4 13 6.3 13z" p-id="5816"></path><path d="M878 626h-60c-4.4 0-8 3.6-8 8v154H214V634c0-4.4-3.6-8-8-8h-60c-4.4 0-8 3.6-8 8v198c0 17.7 14.3 32 32 32h684c17.7 0 32-14.3 32-32V634c0-4.4-3.6-8-8-8z" p-id="5817"></path></svg>&nbsp;Export</el-button>
        </div>
    </div>
    <div style="height: calc(100vh - 50px ); width: 100%; display: flex;">
        <div style="height: calc((40% - 10px)); width: calc(20% - 10px); margin-left: 10px; margin-bottom: 10px; padding: 8px; position: absolute; top: 0px;"
            class="boundary">
            <DataTable />
        </div>

        <div style="height: calc((60% - 0px) - 10px); width: calc(20% - 10px); margin-left: 10px; margin-bottom: 10px; padding: 8px; position: absolute; bottom: 0px;"
            class="boundary">
            <DataDescription />
        </div>
        <div style="height: calc(100% - 10px); width: calc(80% - 10px - 370px); margin-left: 10px; margin-bottom: 10px; padding: 8px; position: absolute; left: calc(20% - 0px);"
            class="boundary">
            <Main />
        </div>
        <div style="height: calc(100% - 10px); width: calc(350px); margin-left: 10px; margin-bottom: 10px; padding: 8px; position: absolute; right: 10px;"
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
// import {Upload, Download} from '@element-plus/icons-vue';

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
