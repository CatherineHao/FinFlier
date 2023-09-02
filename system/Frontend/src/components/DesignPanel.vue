<!--
 * @Description: 
 * @Author: Qing Shi
 * @Date: 2023-08-22 15:08:37
 * @LastEditors: Qing Shi
 * @LastEditTime: 2023-08-29 20:33:06
-->
<template>
    <div class="design_container">
        <div
            style="font-family: KoHo, 'operator Mono Lig'; font-size: 22px;  height: 40px; text-align: start; font-weight: bold;">

            <img src="../assets/img/4.png" width="25" alt="">&nbsp; Design Panel
            <hr>
        </div>
        <!-- <v-expand-transition> -->
        <div v-show="expand" style="overflow-y: scroll; height: calc(100% - 40px);">
            <div class="EditPanel">
                <div class="chartEdit">
                    <h3 class="background">
                        <span>Chart</span>
                    </h3>
                    <div class="sq_collapse">
                        <div class="sq_collapse_item">
                            <div class="sq_collapse_title">
                                <span class="sq_collapse_text">Canvas</span>
                                <!-- <i style="height: 12px; width: 12px;"> -->
                                <div style="height: 20px; width: 30px; cursor: pointer; display: flex; justify-content: flex-end
                                ; align-items: center;" @click="isExpand[0] = !isExpand[0]">
                                    <svg style="height: 12px; width: 12px;" viewBox="0 0 1024 1024"
                                        xmlns="http://www.w3.org/2000/svg">
                                        <path fill="currentColor" v-if="isExpand[0] == 0"
                                            d="M340.864 149.312a30.592 30.592 0 0 0 0 42.752L652.736 512 340.864 831.872a30.592 30.592 0 0 0 0 42.752 29.12 29.12 0 0 0 41.728 0L714.24 534.336a32 32 0 0 0 0-44.672L382.592 149.376a29.12 29.12 0 0 0-41.728 0z">
                                        </path>
                                        <path fill="currentColor" v-if="isExpand[0] == 1"
                                            d="M831.872 340.864 512 652.672 192.128 340.864a30.592 30.592 0 0 0-42.752 0 29.12 29.12 0 0 0 0 41.6L489.664 714.24a32 32 0 0 0 44.672 0l340.288-331.712a29.12 29.12 0 0 0 0-41.728 30.592 30.592 0 0 0-42.752 0z">
                                        </path>
                                    </svg>
                                </div>
                            </div>
                            <el-collapse-transition>
                                <div class="" v-if="isExpand[0] == 1">
                                    <div>Theme</div>
                                    <color-picker v-model="currentColor"></color-picker>
                                </div>
                            </el-collapse-transition>
                        </div>
                        <div class="sq_collapse_item">
                            <div class="sq_collapse_title">
                                <span class="sq_collapse_text">{{ chartType }}</span>
                                <!-- <i style="height: 12px; width: 12px;"> -->
                                <div style="height: 20px; width: 30px; cursor: pointer; display: flex; justify-content: flex-end
                                ; align-items: center;" @click="isExpand[1] = !isExpand[1]">
                                    <svg style="height: 12px; width: 12px;" viewBox="0 0 1024 1024"
                                        xmlns="http://www.w3.org/2000/svg">
                                        <path fill="currentColor" v-if="isExpand[1] == 0"
                                            d="M340.864 149.312a30.592 30.592 0 0 0 0 42.752L652.736 512 340.864 831.872a30.592 30.592 0 0 0 0 42.752 29.12 29.12 0 0 0 41.728 0L714.24 534.336a32 32 0 0 0 0-44.672L382.592 149.376a29.12 29.12 0 0 0-41.728 0z">
                                        </path>
                                        <path fill="currentColor" v-if="isExpand[1] == 1"
                                            d="M831.872 340.864 512 652.672 192.128 340.864a30.592 30.592 0 0 0-42.752 0 29.12 29.12 0 0 0 0 41.6L489.664 714.24a32 32 0 0 0 44.672 0l340.288-331.712a29.12 29.12 0 0 0 0-41.728 30.592 30.592 0 0 0-42.752 0z">
                                        </path>
                                    </svg>
                                </div>
                            </div>
                            <el-collapse-transition>
                                <div class="" v-if="isExpand[1] == 1">
                                    <component :is="tabs[chartType]" v-model="chartSetting"></component>
                                </div>
                            </el-collapse-transition>
                        </div>
                    </div>
                </div>
                <div class="overlayEdit">
                    <h3 class="background">
                        <span>Graphical Overlay</span>
                    </h3>
                    <div class="sq_collapse">
                        <div class="sq_collapse_item">
                            <div class="sq_collapse_title">
                                <div style="display: flex;">
                                    <div style="padding-top: 1.5px; height: 10px;"><el-checkbox v-model="overlayTag[0]"
                                            label="" style="height: 14px; margin-top: 0px;" /> &nbsp;</div>
                                    <span class="sq_collapse_text">Color</span>
                                </div>
                                <div style="height: 20px; width: 30px; cursor: pointer; display: flex; justify-content: flex-end
                                ; align-items: center;" @click="overlayExpand[0] = !overlayExpand[0]">
                                    <svg style="height: 12px; width: 12px;" viewBox="0 0 1024 1024"
                                        xmlns="http://www.w3.org/2000/svg">
                                        <path fill="currentColor" v-if="overlayExpand[0] == 0"
                                            d="M340.864 149.312a30.592 30.592 0 0 0 0 42.752L652.736 512 340.864 831.872a30.592 30.592 0 0 0 0 42.752 29.12 29.12 0 0 0 41.728 0L714.24 534.336a32 32 0 0 0 0-44.672L382.592 149.376a29.12 29.12 0 0 0-41.728 0z">
                                        </path>
                                        <path fill="currentColor" v-if="overlayExpand[0] == 1"
                                            d="M831.872 340.864 512 652.672 192.128 340.864a30.592 30.592 0 0 0-42.752 0 29.12 29.12 0 0 0 0 41.6L489.664 714.24a32 32 0 0 0 44.672 0l340.288-331.712a29.12 29.12 0 0 0 0-41.728 30.592 30.592 0 0 0-42.752 0z">
                                        </path>
                                    </svg>
                                </div>
                            </div>
                            <el-collapse-transition>
                                <!-- <v-expand-transition> -->
                                <div class="sq_collapse_content" v-if="overlayExpand[0] == 1">
                                    <div>Fill</div>
                                    <color-picker v-model="overlaySetting[overlay_map[0]].currentColor"></color-picker>
                                </div>
                                <!-- </v-expand-transition> -->
                            </el-collapse-transition>
                        </div>
                        <div class="sq_collapse_item">
                            <div class="sq_collapse_title">
                                <div style="display: flex;">
                                    <div style="padding-top: 1.5px; height: 10px;"><el-checkbox v-model="overlayTag[1]"
                                            label="" style="height: 14px; margin-top: 0px;" /> &nbsp;</div>
                                    <span class="sq_collapse_text">Bounding Box</span>
                                </div>
                                <div style="height: 20px; width: 30px; cursor: pointer; display: flex; justify-content: flex-end
                                ; align-items: center;" @click="overlayExpand[1] = !overlayExpand[1]">
                                    <svg style="height: 12px; width: 12px;" viewBox="0 0 1024 1024"
                                        xmlns="http://www.w3.org/2000/svg">
                                        <path fill="currentColor" v-if="overlayExpand[1] == 0"
                                            d="M340.864 149.312a30.592 30.592 0 0 0 0 42.752L652.736 512 340.864 831.872a30.592 30.592 0 0 0 0 42.752 29.12 29.12 0 0 0 41.728 0L714.24 534.336a32 32 0 0 0 0-44.672L382.592 149.376a29.12 29.12 0 0 0-41.728 0z">
                                        </path>
                                        <path fill="currentColor" v-if="overlayExpand[1] == 1"
                                            d="M831.872 340.864 512 652.672 192.128 340.864a30.592 30.592 0 0 0-42.752 0 29.12 29.12 0 0 0 0 41.6L489.664 714.24a32 32 0 0 0 44.672 0l340.288-331.712a29.12 29.12 0 0 0 0-41.728 30.592 30.592 0 0 0-42.752 0z">
                                        </path>
                                    </svg>
                                </div>
                            </div>
                            <el-collapse-transition>
                                <div class="sq_collapse_content" v-if="overlayExpand[1] == 1">
                                    <div>Stroke</div>
                                    <color-picker v-model="overlaySetting[overlay_map[1]].currentColor"></color-picker>
                                </div>
                            </el-collapse-transition>
                        </div>
                        <div class="sq_collapse_item">
                            <div class="sq_collapse_title">
                                <div style="display: flex;">
                                    <div style="padding-top: 1.5px; height: 10px;"><el-checkbox v-model="overlayTag[2]"
                                            label="" style="height: 14px; margin-top: 0px;" /> &nbsp;</div>
                                    <span class="sq_collapse_text">Background</span>
                                </div>
                                <div style="height: 20px; width: 30px; cursor: pointer; display: flex; justify-content: flex-end
                                ; align-items: center;" @click="overlayExpand[2] = !overlayExpand[2]">
                                    <svg style="height: 12px; width: 12px;" viewBox="0 0 1024 1024"
                                        xmlns="http://www.w3.org/2000/svg">
                                        <path fill="currentColor" v-if="overlayExpand[2] == 0"
                                            d="M340.864 149.312a30.592 30.592 0 0 0 0 42.752L652.736 512 340.864 831.872a30.592 30.592 0 0 0 0 42.752 29.12 29.12 0 0 0 41.728 0L714.24 534.336a32 32 0 0 0 0-44.672L382.592 149.376a29.12 29.12 0 0 0-41.728 0z">
                                        </path>
                                        <path fill="currentColor" v-if="overlayExpand[2] == 1"
                                            d="M831.872 340.864 512 652.672 192.128 340.864a30.592 30.592 0 0 0-42.752 0 29.12 29.12 0 0 0 0 41.6L489.664 714.24a32 32 0 0 0 44.672 0l340.288-331.712a29.12 29.12 0 0 0 0-41.728 30.592 30.592 0 0 0-42.752 0z">
                                        </path>
                                    </svg>
                                </div>
                            </div>
                            <el-collapse-transition>
                                <div class="sq_collapse_content" v-if="overlayExpand[2] == 1">
                                    <div>Fill</div>
                                    <color-picker v-model="overlaySetting[overlay_map[2]].currentColor"></color-picker>
                                </div>
                            </el-collapse-transition>
                        </div>
                        <div class="sq_collapse_item">
                            <div class="sq_collapse_title">
                                <div style="display: flex;">
                                    <div style="padding-top: 1.5px; height: 10px;"><el-checkbox v-model="overlayTag[3]"
                                            label="" style="height: 14px; margin-top: 0px;" /> &nbsp;</div>
                                    <span class="sq_collapse_text">Marker</span>
                                </div>
                                <div style="height: 20px; width: 30px; cursor: pointer; display: flex; justify-content: flex-end
                                ; align-items: center;" @click="overlayExpand[3] = !overlayExpand[3]">
                                    <svg style="height: 12px; width: 12px;" viewBox="0 0 1024 1024"
                                        xmlns="http://www.w3.org/2000/svg">
                                        <path fill="currentColor" v-if="overlayExpand[3] == 0"
                                            d="M340.864 149.312a30.592 30.592 0 0 0 0 42.752L652.736 512 340.864 831.872a30.592 30.592 0 0 0 0 42.752 29.12 29.12 0 0 0 41.728 0L714.24 534.336a32 32 0 0 0 0-44.672L382.592 149.376a29.12 29.12 0 0 0-41.728 0z">
                                        </path>
                                        <path fill="currentColor" v-if="overlayExpand[3] == 1"
                                            d="M831.872 340.864 512 652.672 192.128 340.864a30.592 30.592 0 0 0-42.752 0 29.12 29.12 0 0 0 0 41.6L489.664 714.24a32 32 0 0 0 44.672 0l340.288-331.712a29.12 29.12 0 0 0 0-41.728 30.592 30.592 0 0 0-42.752 0z">
                                        </path>
                                    </svg>
                                </div>
                            </div>
                            <el-collapse-transition>
                                <div class="sq_collapse_content" v-if="overlayExpand[3] == 1">
                                    <div>Fill</div>
                                    <color-picker v-model="overlaySetting[overlay_map[3]].currentColor"></color-picker>
                                </div>
                            </el-collapse-transition>
                        </div>
                        <div class="sq_collapse_item">
                            <div class="sq_collapse_title">
                                <div style="display: flex;">
                                    <div style="padding-top: 1.5px; height: 10px;"><el-checkbox v-model="overlayTag[4]"
                                            label="" style="height: 14px; margin-top: 0px;" /> &nbsp;</div>
                                    <span class="sq_collapse_text">Label</span>
                                </div>
                                <div style="height: 20px; width: 30px; cursor: pointer; display: flex; justify-content: flex-end
                                ; align-items: center;" @click="overlayExpand[4] = !overlayExpand[4]">
                                    <svg style="height: 12px; width: 12px;" viewBox="0 0 1024 1024"
                                        xmlns="http://www.w3.org/2000/svg">
                                        <path fill="currentColor" v-if="overlayExpand[4] == 0"
                                            d="M340.864 149.312a30.592 30.592 0 0 0 0 42.752L652.736 512 340.864 831.872a30.592 30.592 0 0 0 0 42.752 29.12 29.12 0 0 0 41.728 0L714.24 534.336a32 32 0 0 0 0-44.672L382.592 149.376a29.12 29.12 0 0 0-41.728 0z">
                                        </path>
                                        <path fill="currentColor" v-if="overlayExpand[4] == 1"
                                            d="M831.872 340.864 512 652.672 192.128 340.864a30.592 30.592 0 0 0-42.752 0 29.12 29.12 0 0 0 0 41.6L489.664 714.24a32 32 0 0 0 44.672 0l340.288-331.712a29.12 29.12 0 0 0 0-41.728 30.592 30.592 0 0 0-42.752 0z">
                                        </path>
                                    </svg>
                                </div>
                            </div>
                            <el-collapse-transition>
                                <div class="sq_collapse_content" v-if="overlayExpand[4] == 1">
                                    <div>Fill</div>
                                    <color-picker v-model="overlaySetting[overlay_map[4]].currentColor"></color-picker>
                                </div>
                            </el-collapse-transition>
                        </div>
                        <div class="sq_collapse_item">
                            <div class="sq_collapse_title">
                                <div style="display: flex;">
                                    <div style="padding-top: 1.5px; height: 10px;"><el-checkbox v-model="overlayTag[5]"
                                            label="" style="height: 14px; margin-top: 0px;" /> &nbsp;</div>
                                    <span class="sq_collapse_text">Text</span>
                                </div>
                                <div style="height: 20px; width: 30px; cursor: pointer; display: flex; justify-content: flex-end
                                ; align-items: center;" @click="overlayExpand[5] = !overlayExpand[5]">
                                    <svg style="height: 12px; width: 12px;" viewBox="0 0 1024 1024"
                                        xmlns="http://www.w3.org/2000/svg">
                                        <path fill="currentColor" v-if="overlayExpand[5] == 0"
                                            d="M340.864 149.312a30.592 30.592 0 0 0 0 42.752L652.736 512 340.864 831.872a30.592 30.592 0 0 0 0 42.752 29.12 29.12 0 0 0 41.728 0L714.24 534.336a32 32 0 0 0 0-44.672L382.592 149.376a29.12 29.12 0 0 0-41.728 0z">
                                        </path>
                                        <path fill="currentColor" v-if="overlayExpand[5] == 1"
                                            d="M831.872 340.864 512 652.672 192.128 340.864a30.592 30.592 0 0 0-42.752 0 29.12 29.12 0 0 0 0 41.6L489.664 714.24a32 32 0 0 0 44.672 0l340.288-331.712a29.12 29.12 0 0 0 0-41.728 30.592 30.592 0 0 0-42.752 0z">
                                        </path>
                                    </svg>
                                </div>
                            </div>
                            <el-collapse-transition>
                                <div class="sq_collapse_content" v-if="overlayExpand[5] == 1">
                                    <div>Fill</div>
                                    <color-picker v-model="overlaySetting[overlay_map[5]].currentColor"></color-picker>
                                </div>
                            </el-collapse-transition>
                        </div>
                        <div class="sq_collapse_item">
                            <div class="sq_collapse_title">
                                <div style="display: flex;">
                                    <div style="padding-top: 1.5px; height: 10px;"><el-checkbox v-model="overlayTag[6]"
                                            label="" style="height: 14px; margin-top: 0px;" /> &nbsp;</div>
                                    <span class="sq_collapse_text">Trend Line</span>
                                </div>
                                <div style="height: 20px; width: 30px; cursor: pointer; display: flex; justify-content: flex-end
                                ; align-items: center;" @click="overlayExpand[6] = !overlayExpand[6]">
                                    <svg style="height: 12px; width: 12px;" viewBox="0 0 1024 1024"
                                        xmlns="http://www.w3.org/2000/svg">
                                        <path fill="currentColor" v-if="overlayExpand[6] == 0"
                                            d="M340.864 149.312a30.592 30.592 0 0 0 0 42.752L652.736 512 340.864 831.872a30.592 30.592 0 0 0 0 42.752 29.12 29.12 0 0 0 41.728 0L714.24 534.336a32 32 0 0 0 0-44.672L382.592 149.376a29.12 29.12 0 0 0-41.728 0z">
                                        </path>
                                        <path fill="currentColor" v-if="overlayExpand[6] == 1"
                                            d="M831.872 340.864 512 652.672 192.128 340.864a30.592 30.592 0 0 0-42.752 0 29.12 29.12 0 0 0 0 41.6L489.664 714.24a32 32 0 0 0 44.672 0l340.288-331.712a29.12 29.12 0 0 0 0-41.728 30.592 30.592 0 0 0-42.752 0z">
                                        </path>
                                    </svg>
                                </div>
                            </div>
                            <el-collapse-transition>
                                <div class="sq_collapse_content" v-if="overlayExpand[6] == 1">
                                    <div>Fill</div>
                                    <color-picker v-model="overlaySetting[overlay_map[6]].currentColor"></color-picker>
                                </div>
                            </el-collapse-transition>
                        </div>
                        <div class="sq_collapse_item">
                            <div class="sq_collapse_title">
                                <div style="display: flex;">
                                    <div style="padding-top: 1.5px; height: 10px;"><el-checkbox v-model="overlayTag[7]"
                                            label="" style="height: 14px; margin-top: 0px;" /> &nbsp;</div>
                                    <span class="sq_collapse_text">Overall Indicator</span>
                                </div>
                                <div style="height: 20px; width: 30px; cursor: pointer; display: flex; justify-content: flex-end
                                ; align-items: center;" @click="overlayExpand[7] = !overlayExpand[7]">
                                    <svg style="height: 12px; width: 12px;" viewBox="0 0 1024 1024"
                                        xmlns="http://www.w3.org/2000/svg">
                                        <path fill="currentColor" v-if="overlayExpand[7] == 0"
                                            d="M340.864 149.312a30.592 30.592 0 0 0 0 42.752L652.736 512 340.864 831.872a30.592 30.592 0 0 0 0 42.752 29.12 29.12 0 0 0 41.728 0L714.24 534.336a32 32 0 0 0 0-44.672L382.592 149.376a29.12 29.12 0 0 0-41.728 0z">
                                        </path>
                                        <path fill="currentColor" v-if="overlayExpand[7] == 1"
                                            d="M831.872 340.864 512 652.672 192.128 340.864a30.592 30.592 0 0 0-42.752 0 29.12 29.12 0 0 0 0 41.6L489.664 714.24a32 32 0 0 0 44.672 0l340.288-331.712a29.12 29.12 0 0 0 0-41.728 30.592 30.592 0 0 0-42.752 0z">
                                        </path>
                                    </svg>
                                </div>
                            </div>
                            <el-collapse-transition>
                                <div class="sq_collapse_content" v-if="overlayExpand[7] == 1">
                                    <div>Fill</div>
                                    <color-picker v-model="overlaySetting[overlay_map[7]].currentColor"></color-picker>
                                </div>
                            </el-collapse-transition>
                        </div>
                        <div class="sq_collapse_item">
                            <div class="sq_collapse_title">
                                <div style="display: flex;">
                                    <div style="padding-top: 1.5px; height: 10px;"><el-checkbox v-model="overlayTag[8]"
                                            label="" style="height: 14px; margin-top: 0px;" /> &nbsp;</div>
                                    <span class="sq_collapse_text">Special Time-point</span>
                                </div>
                                <div style="height: 20px; width: 30px; cursor: pointer; display: flex; justify-content: flex-end
                                ; align-items: center;" @click="overlayExpand[8] = !overlayExpand[8]">
                                    <svg style="height: 12px; width: 12px;" viewBox="0 0 1024 1024"
                                        xmlns="http://www.w3.org/2000/svg">
                                        <path fill="currentColor" v-if="overlayExpand[8] == 0"
                                            d="M340.864 149.312a30.592 30.592 0 0 0 0 42.752L652.736 512 340.864 831.872a30.592 30.592 0 0 0 0 42.752 29.12 29.12 0 0 0 41.728 0L714.24 534.336a32 32 0 0 0 0-44.672L382.592 149.376a29.12 29.12 0 0 0-41.728 0z">
                                        </path>
                                        <path fill="currentColor" v-if="overlayExpand[8] == 1"
                                            d="M831.872 340.864 512 652.672 192.128 340.864a30.592 30.592 0 0 0-42.752 0 29.12 29.12 0 0 0 0 41.6L489.664 714.24a32 32 0 0 0 44.672 0l340.288-331.712a29.12 29.12 0 0 0 0-41.728 30.592 30.592 0 0 0-42.752 0z">
                                        </path>
                                    </svg>
                                </div>
                            </div>
                            <el-collapse-transition>
                                <div class="sq_collapse_content" v-if="overlayExpand[8] == 1">
                                    <div>Fill</div>
                                    <color-picker v-model="overlaySetting[overlay_map[8]].currentColor"></color-picker>
                                </div>
                            </el-collapse-transition>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- </v-expand-transition> -->
    </div>
</template>

<script>
import { useDataStore } from "../stores/counter";
import ColorPicker from './utils/ColorPicker.vue';
import singleBarPanel from "./utils/singleBarPanel.vue";
export default {
    name: "DesignPanel",
    props: [],
    data () {
        return {
            msg1: "Hello, main!",
            currentColor: { r: 255, g: 30, b: 20, a: 0.5 },
            isExpand: [0, 1],
            overlayExpand: [0, 0, 0, 0, 0, 0, 0, 0, 0],
            overlayTag: [0, 0, 0, 0, 0, 0, 0, 0, 0],
            expand: false,
            chartType: "",
            tabs: {
                'Single bar chart': 'singleBarPanel'
            },
            chartSetting: {},
            overlaySetting: {},
            overlay_map: ['color', 'bounding box', 'background', 'marker', 'label', 'text', 'trend', 'overall', 'special'],
        };
    },
    methods: {},
    created () { },
    computed: {},
    mounted () {
        const dataStore = useDataStore();
        this.rawData = dataStore.data;
        // [this.th, this.td] = this.calcTable(this.rawData);
        // console.log(this.rawData)
        setTimeout(() => this.expand = !this.expand, 100);
        dataStore.$subscribe((mutations) => {

            // if (mutations.events.key == 'chart_data') {
            this.chartType = dataStore.chart_data['chartType'];
            this.chartSetting = dataStore.state_map['state0']['chart_setting'];
            this.overlaySetting = dataStore.state_map['state0']['overlay_setting']['object0'];
            
            // }
        })
    },
    components: {
        'color-picker': ColorPicker,
        'singleBarPanel': singleBarPanel
    },
    watch: {
        chartSetting: {
            handler (newVal) {
                const dataStore = useDataStore();
                dataStore.state_map['state0']['chart_setting'] = newVal;
            },
            deep: true // 监听嵌套属性的变化
        },
        overlaySetting: {
            handler (newVal) {
                const dataStore = useDataStore();
                dataStore.state_map['state0']['overlay_setting']['object0'] = newVal;
            },
            deep: true // 监听嵌套属性的变化
        },
        overlayTag: {
            handler (newVal, oldVal) {
                // const dataStore = useDataStore();
                // console.log(newVal)
                for (let i in newVal) {
                    // if (newVal[i] != oldVal[i]) {
                        if (newVal[i] == 1) {
                            this.overlayExpand[i] = 1;
                        } else {
                            this.overlayExpand[i] = 0;
                        }
                    // }
                }
                const dataStore = useDataStore();
                // console.log(dataStore.state_map['state0'])
                dataStore.state_map['state0']['overlay_tag'] = newVal;
            },
            deep: true // 监听嵌套属性的变化
        }
    }
}
</script>

<style scoped>
.design_container {
    text-align: start;
    height: 100%;
}

h3 {
    margin-top: 10px;
    text-align: center;
    text-transform: uppercase;
    background: #fff;
    font-family: "DM Sans", sans-serif;
    color: #2a2a2a;
    font-size: 16px;
    font-weight: 600;
    margin-bottom: 10px;
}

h3.background {
    position: relative;
    z-index: 1;

    &:before {
        border-top: 1px solid #2a2a2a;
        content: "";
        margin: 0 auto;
        /* this centers the line to the full width specified */
        position: absolute;
        /* positioning must be absolute here, and relative positioning must be applied to the parent */
        top: 50%;
        left: 0;
        right: 0;
        bottom: 0;
        width: 95%;
        z-index: -1;
    }
}

h3 span {
    /* to hide the lines from behind the text, you have to set the background color the same as the container */
    background: #fff;
    padding: 0 15px;
}

.EditInfo {
    text-align: start;
}

.EditPanel {
    overflow-y: auto;
    scroll-behavior: smooth;
}

.sq_collapse {
    border-top: 1px solid rgba(99, 99, 99, 0.3);
    width: 100%;
    /* border-bottom: 1px solid rgba(99, 99, 99, 0.3); */
}

.sq_collapse_item {
    border-bottom: 1px solid rgba(99, 99, 99, 0.3);
    padding: 5px;
    width: 100%;
}

.sq_collapse_title {
    width: 100%;
    text-align: start;
    display: flex;
    align-items: center;
    justify-content: space-between;
    /* display: flex;
    align-items: center; */
}

.sq_collapse_text {
    font-weight: bold;
}

.sq_collapse_content {
    /* padding: 10px 0px 10px 0px; */
}
</style>
