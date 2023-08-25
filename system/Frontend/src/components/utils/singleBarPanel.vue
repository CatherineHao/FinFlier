<template>
    <div>
        <div>Fill</div>
        <color-picker v-model="chartSetting.currentColor"></color-picker>
        <div>Size</div>
        <div>Width: <input class="widthInput" v-model="chartSetting.size.width" placeholder="Please input" /> px</div>
        <div>Axis</div>
        <div style="display: flex;">
            <div style="width: 20px;">X:</div>
            <input class="axisInput" v-model="chartSetting.axis.x" placeholder="Please input" />
        </div>
        <div style="display: flex; margin-top: 5px;">
            <div style="width: 20px;">Y:</div>
            <input class="axisInput" v-model="chartSetting.axis.y" placeholder="Please input" />
        </div>
    </div>
</template>
<script>
import ColorPicker from './ColorPicker.vue';
export default {
    name: "singleBarPanel",
    props: {
        modelValue: Object
    },
    data () {
        return {
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
                }
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

.widthInput {
    width: 60px;
    border: 1px solid #ccc;
    border-radius: 5px;
    padding-left: 3px;
    padding-right: 3px;
}

.axisInput {
    width: calc(100% - 30px);
    border: 1px solid #ccc;
    border-radius: 5px;
    padding-left: 3px;
    padding-right: 3px;

}</style>
