<template>
    <div>
        <div style="display: flex; margin-top: 5px;">
            <div style="margin-right: 10px;">Legend</div>
            <div><el-checkbox v-model="chartSetting.isLegend" label="" style="height: 14px; margin-top: 4px;" /></div>
        </div>
        <div>
            <div style="display: flex; margin-bottom: 5px; align-items: center;" v-for="(item, i) in chartSetting.attrName">
                <div style="width: 50px;">Label:</div>
                <div style="margin-right: 5px;">
                    <color-picker v-model="chartSetting.currentColor[item]"></color-picker>
                </div>
                <input class="axisInput" style="width: calc(100% - 85px);" v-model="chartSetting.attrName[i]" placeholder="Please input" />
            </div>
        </div>
        <hr>
        <div>Bar Size</div>
        <div>Width: <input class="widthInput" v-model="chartSetting.size.width" placeholder="Please input" /> px</div>
        <hr>
        <div>Title</div>
        <div style="display: flex;">
            <div style="width: 50px;">Label:</div>
            <input class="axisInput" v-model="chartSetting.title" placeholder="Please input" />
        </div>
        <div>X Axis</div>
        <div style="display: flex;">
            <div style="width: 50px;">Label:</div>
            <input class="axisInput" v-model="chartSetting.axis.x" placeholder="Please input" />
        </div>
        <div>Y Axis</div>
        <div style="display: flex; margin-top: 5px;">
            <div style="width: 50px;">Label:</div>
            <input class="axisInput" v-model="chartSetting.axis.y" placeholder="Please input" />
        </div>
        <!-- <div style="display: flex; margin-top: 5px;">
            <div style="margin-right: 10px;">Legend</div>
            <div><el-checkbox v-model="chartSetting.isLegend" label="" style="height: 14px; margin-top: 0px;" /></div>
        </div> -->
    </div>
</template>
<script>
import ColorPicker from './ColorPicker_single.vue';
export default {
    name: "singleBarPanel",
    props: {
        modelValue: Object
    },
    data () {
        return {
            // isLegend: true÷÷,
            chartSetting: {
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
                },
                isLegend: 1,
                yName: 'aaaa'
            }
        };
    },
    methods: {
    },
    created () {
    },
    computed: {
    },
    mounted () {
    },
    watch: {
        modelValue: {
            handler (newValue) {
                this.chartSetting = newValue;
            },
            immediate: true // 在组件创建时立即触发
        },
        // 监听currentColor的变化，并将其同步到外部modelValue
        chartSetting: {
            handler (newVal) {
                this.$emit('update:modelValue', newVal);
            },
            deep: true // 监听嵌套属性的变化
        }
    },
    components: {
        'color-picker': ColorPicker
    }
}
</script>
<style scoped>
.container {
    display: flex;
    text-align: start;
    align-items: center;
    font-size: 14px;
}

hr {
    margin-top: 5px;
}

.widthInput {
    width: 60px;
    border: 1px solid #ccc;
    border-radius: 5px;
    padding-left: 3px;
    padding-right: 3px;
}

.axisInput {
    width: calc(100% - 60px);
    border: 1px solid #ccc;
    border-radius: 5px;
    padding-left: 3px;
    padding-right: 3px;
}
</style>
