<!--
 * @Description: 
 * @Author: Qing Shi
 * @Date: 2022-09-17 23:36:36
 * @LastEditTime: 2023-02-13 11:02:16
-->
<template>
    <div class="common-layout" style="width: 100%; height: 100vh; background-color: white;">
        <div style="padding-top: 30vh;font-style: italic; font-family: 'operator Mono Lig'; font-size: 50px;">
            FinTeller
            <br />
            <!-- <v-btn variant="tonal">
                Upload Data
            </v-btn> -->
            <el-upload style="height: 30px;" class="upload-demo" action="" :http-request="uploadFile" accept=".csv" :show-file-list="false">
                <v-btn variant="tonal">
                    Upload Dataset
                </v-btn>
            </el-upload>
        </div>
    </div>
</template>

<script>
import Main from '../components/Main.vue';
import { useDataStore } from "../stores/counter";
import { csv } from "d3";

export default {
    name: "upload dataset",
    data () {
        return {
            msgH: null,
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
    },
    methods: {
        fetchData () {
        },
        jump(url) {
            this.$router.push({
                path: `/${url}`
            });
        },
        async uploadFile(params) {
            let fileObj = params.file;
            let form = new FormData();
            form.append("fileToUpload", fileObj);
            let file_name = form.get("fileToUpload").name;
            const data = await csv('/src/assets/data/' + file_name);
            const dataStore = useDataStore();
            dataStore.data = data;
            // console.log(dataStore.data);
            dataStore.fetchBasicChart({
                data: data
            })
            this.jump('home');
        }
    },
    components: { Main }
};
</script>
<style scoped>

.boundary {
    /*border-style: dashed;*/
    border-style: solid;
    border-color: #d3dce6;
    border-width: 0.5px;
    border-radius: 3px;
}
</style>
