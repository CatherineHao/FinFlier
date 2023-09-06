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
                                <span class="sq_collapse_text"><svg t="1693753372823" class="icon" viewBox="0 0 1024 1024"
                                        version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="4088" width="20" height="20">
                                        <path
                                            d="M938.666667 704a21.333333 21.333333 0 0 0-21.333334-21.333333H896V256a85.333333 85.333333 0 0 0-85.333333-85.333333h-256V106.666667a21.333333 21.333333 0 0 0-21.333334-21.333334h-42.666666a21.333333 21.333333 0 0 0-21.333334 21.333334V170.666667H213.333333a85.333333 85.333333 0 0 0-85.333333 85.333333v426.666667h-21.333333a21.333333 21.333333 0 0 0-21.333334 21.333333v42.666667a21.333333 21.333333 0 0 0 21.333334 21.333333h205.226666l-92.586666 132.266667a32.426667 32.426667 0 0 0-5.973334 18.346666v9.386667a10.666667 10.666667 0 0 0 10.666667 10.666667h50.346667a42.666667 42.666667 0 0 0 34.986666-18.346667L416 768h192l106.666667 152.32a42.666667 42.666667 0 0 0 34.986666 18.346667h50.346667a10.666667 10.666667 0 0 0 10.666667-10.666667v-9.386667a32.426667 32.426667 0 0 0-5.973334-18.346666L712.106667 768h205.226666a21.333333 21.333333 0 0 0 21.333334-21.333333z m-128-21.333333H213.333333V256h597.333334z"
                                            p-id="4089"></path>
                                    </svg>&nbsp;Canvas</span>
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
                                <div class="sq_collapse_content" v-if="isExpand[0] == 1">
                                    <div>Theme</div>
                                    <color-picker v-model="currentColor"></color-picker>
                                </div>
                            </el-collapse-transition>
                        </div>
                        <div class="sq_collapse_item">
                            <div class="sq_collapse_title">
                                <span class="sq_collapse_text"><svg v-if="chartType == 1 ||  chartType == 3" t="1693879259065" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="7748" width="20" height="20"><path d="M888 792H200V168c0-4.4-3.6-8-8-8h-56c-4.4 0-8 3.6-8 8v688c0 4.4 3.6 8 8 8h752c4.4 0 8-3.6 8-8v-56c0-4.4-3.6-8-8-8z" p-id="7749"></path><path d="M305.8 637.7c3.1 3.1 8.1 3.1 11.3 0l138.3-137.6L583 628.5c3.1 3.1 8.2 3.1 11.3 0l275.4-275.3c3.1-3.1 3.1-8.2 0-11.3l-39.6-39.6c-3.1-3.1-8.2-3.1-11.3 0l-230 229.9L461.4 404c-3.1-3.1-8.2-3.1-11.3 0L266.3 586.7c-3.1 3.1-3.1 8.2 0 11.3l39.5 39.7z" p-id="7750"></path></svg><svg v-else t="1693879354394" class="icon" viewBox="0 0 1184 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="8865" width="20" height="20"><path d="M365.728 512l0 292.576-146.272 0 0-292.576 146.272 0zM585.152 219.424l0 585.152-146.272 0 0-585.152 146.272 0zM1170.272 877.728l0 73.152-1170.272 0 0-877.728 73.152 0 0 804.576 1097.152 0zM804.576 365.728l0 438.848-146.272 0 0-438.848 146.272 0zM1024 146.272l0 658.272-146.272 0 0-658.272 146.272 0z" p-id="8866"></path></svg>&nbsp;{{ chartTypeMap[chartType] }}</span>
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
                                <div class="sq_collapse_content" v-if="isExpand[1] == 1">
                                    <component :is="tabs[chartTypeMap[chartType]]" v-model="chartSetting"></component>
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
                                    <span class="sq_collapse_text"><svg t="1693753704635" class="icon"
                                            viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
                                            p-id="12736" width="20" height="20">
                                            <path
                                                d="M766.4 744.3c43.7 0 79.4-36.2 79.4-80.5 0-53.5-79.4-140.8-79.4-140.8S687 610.3 687 663.8c0 44.3 35.7 80.5 79.4 80.5zM389.3 700.2c7.1 7.1 18.6 7.1 25.6 0l256.1-256c7.1-7.1 7.1-18.6 0-25.6l-256-256c-0.6-0.6-1.3-1.2-2-1.7l-78.2-78.2c-3.5-3.5-9.3-3.5-12.8 0l-48 48c-3.5 3.5-3.5 9.3 0 12.8l67.2 67.2-207.8 207.9c-7.1 7.1-7.1 18.6 0 25.6l255.9 256z m12.9-448.6l178.9 178.9H223.4l178.8-178.9zM904 816H120c-4.4 0-8 3.6-8 8v80c0 4.4 3.6 8 8 8h784c4.4 0 8-3.6 8-8v-80c0-4.4-3.6-8-8-8z"
                                                p-id="12737"></path>
                                        </svg>&nbsp;Highlight</span>
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
                                    <span class="sq_collapse_text"><svg t="1693753657778" class="icon"
                                            viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
                                            p-id="11647" width="20" height="20">
                                            <path
                                                d="M170.922667 127.573333a42.666667 42.666667 0 0 0-42.666667 42.666667v170.666667a42.666667 42.666667 0 0 0 42.666667 42.666666h42.666666v256h-42.666666a42.666667 42.666667 0 0 0-42.666667 42.666667v170.666667a42.666667 42.666667 0 0 0 42.666667 42.666666h170.666666a42.666667 42.666667 0 0 0 42.666667-42.666666v-42.666667h256v42.666667a42.666667 42.666667 0 0 0 42.666667 42.666666h170.666666a42.666667 42.666667 0 0 0 42.666667-42.666666v-170.666667a42.666667 42.666667 0 0 0-42.666667-42.666667h-42.666666v-256h42.666666a42.666667 42.666667 0 0 0 42.666667-42.666666v-170.666667a42.666667 42.666667 0 0 0-42.666667-42.666667h-170.666666a42.666667 42.666667 0 0 0-42.666667 42.666667v42.666667h-256v-42.666667a42.666667 42.666667 0 0 0-42.666667-42.666667h-170.666666z m42.666666 85.333334h85.333334v85.333333h-85.333334v-85.333333z m512 0h85.333334v85.333333h-85.333334v-85.333333z m-341.333333 85.333333h256v42.666667a42.666667 42.666667 0 0 0 42.666667 42.666666h42.666666v256h-42.666666a42.666667 42.666667 0 0 0-42.666667 42.666667v42.666667h-256v-42.666667a42.666667 42.666667 0 0 0-42.666667-42.666667h-42.666666v-256h42.666666a42.666667 42.666667 0 0 0 42.666667-42.666666v-42.666667z m-170.666667 426.666667h85.333334v85.333333h-85.333334v-85.333333z m512 0h85.333334v85.333333h-85.333334v-42.666667-42.666666z"
                                                fill="#000000" p-id="11648"></path>
                                        </svg>&nbsp;Bounding Box</span>
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
                                    <span class="sq_collapse_text"><svg t="1693753616043" class="icon"
                                            viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
                                            p-id="10642" width="20" height="20">
                                            <path
                                                d="M902.095238 213.942857v103.424L317.318095 902.095238H213.894095L902.095238 213.942857z m0 277.942857v103.424L595.260952 902.095238h-103.448381L902.095238 491.885714z m0 277.942857v103.424L873.20381 902.095238h-103.424L902.095238 769.828571zM819.590095 121.904762L121.904762 819.614476v-103.424L716.190476 121.904762h103.424z m-277.942857 0L121.904762 541.671619v-103.424L438.223238 121.904762h103.448381z m-277.942857 0L121.904762 263.728762V160.304762L160.304762 121.904762h103.424z"
                                                p-id="10643"></path>
                                        </svg>&nbsp;Background</span>
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
                                    <span class="sq_collapse_text"><svg t="1693753751051" class="icon"
                                            viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
                                            p-id="13722" width="20" height="20">
                                            <path
                                                d="M512 0C299.2 0 128 179.2 128 404.8c0 192 264 507.2 345.6 601.6 8 12.8 25.6 17.6 38.4 17.6 17.6 0 30.4-8 38.4-17.6C632 913.6 896 593.6 896 404.8 896 179.2 724.8 0 512 0z m0 921.6c-145.6-171.2-299.2-396.8-299.2-516.8 0-179.2 132.8-320 299.2-320s299.2 145.6 299.2 320c0 120-153.6 345.6-299.2 516.8z"
                                                p-id="13723"></path>
                                            <path
                                                d="M512 212.8c-94.4 0-171.2 76.8-171.2 171.2S417.6 555.2 512 555.2 683.2 478.4 683.2 384 606.4 212.8 512 212.8z m0 256c-46.4 0-84.8-38.4-84.8-84.8s38.4-84.8 84.8-84.8 84.8 38.4 84.8 84.8-38.4 84.8-84.8 84.8z"
                                                p-id="13724"></path>
                                        </svg>&nbsp;Marker</span>
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
                                    <span class="sq_collapse_text"><svg t="1693795828843" class="icon"
                                            viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
                                            p-id="24037" width="20" height="20">
                                            <path
                                                d="M562.873 99.366a31.976 31.976 0 0 1 27.132-9.044l276.973 39.567a31.976 31.976 0 0 1 27.133 27.133l39.567 276.973a31.976 31.976 0 0 1-9.044 27.132L461.127 924.635c-12.487 12.487-32.733 12.487-45.22 0L99.365 608.093c-12.487-12.487-12.487-32.733 0-45.22L562.873 99.366z m39.567 73.483L189.806 585.483l248.711 248.711L851.151 421.56l-31.088-217.623L602.44 172.85z m16.958 118.703c31.218-31.218 81.832-31.218 113.05 0 31.218 31.218 31.218 81.832 0 113.05-31.218 31.218-81.832 31.218-113.05 0-31.218-31.218-31.218-81.832 0-113.05z"
                                                fill="#2c2c2c" p-id="24038"></path>
                                        </svg>&nbsp;Label</span>
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
                                    <span class="sq_collapse_text"><svg t="1693753854090" class="icon"
                                            viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
                                            p-id="16686" width="20" height="20">
                                            <path
                                                d="M853.333333 1024 170.666667 1024c-93.866667 0-170.666667-76.8-170.666667-170.666667L0 170.666667c0-93.866667 76.8-170.666667 170.666667-170.666667l682.666667 0c93.866667 0 170.666667 76.8 170.666667 170.666667l0 682.666667C1024 947.2 947.2 1024 853.333333 1024zM170.666667 85.333333C123.733333 85.333333 85.333333 123.733333 85.333333 170.666667l0 682.666667c0 46.933333 38.4 85.333333 85.333333 85.333333l682.666667 0c46.933333 0 85.333333-38.4 85.333333-85.333333L938.666667 170.666667c0-46.933333-38.4-85.333333-85.333333-85.333333L170.666667 85.333333z"
                                                p-id="16687"></path>
                                            <path
                                                d="M725.333333 341.333333 298.666667 341.333333C273.066667 341.333333 256 324.266667 256 298.666667s17.066667-42.666667 42.666667-42.666667l426.666667 0c25.6 0 42.666667 17.066667 42.666667 42.666667S750.933333 341.333333 725.333333 341.333333z"
                                                p-id="16688"></path>
                                            <path
                                                d="M298.666667 384C273.066667 384 256 366.933333 256 341.333333L256 298.666667c0-25.6 17.066667-42.666667 42.666667-42.666667s42.666667 17.066667 42.666667 42.666667l0 42.666667C341.333333 366.933333 324.266667 384 298.666667 384z"
                                                p-id="16689"></path>
                                            <path
                                                d="M725.333333 384c-25.6 0-42.666667-17.066667-42.666667-42.666667L682.666667 298.666667c0-25.6 17.066667-42.666667 42.666667-42.666667s42.666667 17.066667 42.666667 42.666667l0 42.666667C768 366.933333 750.933333 384 725.333333 384z"
                                                p-id="16690"></path>
                                            <path
                                                d="M512 768c-25.6 0-42.666667-17.066667-42.666667-42.666667L469.333333 298.666667c0-25.6 17.066667-42.666667 42.666667-42.666667s42.666667 17.066667 42.666667 42.666667l0 426.666667C554.666667 750.933333 537.6 768 512 768z"
                                                p-id="16691"></path>
                                            <path
                                                d="M554.666667 768l-85.333333 0c-25.6 0-42.666667-17.066667-42.666667-42.666667s17.066667-42.666667 42.666667-42.666667l85.333333 0c25.6 0 42.666667 17.066667 42.666667 42.666667S580.266667 768 554.666667 768z"
                                                p-id="16692"></path>
                                        </svg>&nbsp;Description</span>
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
                                    <span class="sq_collapse_text"><svg t="1693753924575" class="icon"
                                            viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
                                            p-id="17658" width="20" height="20">
                                            <path
                                                d="M891.733333 605.44c-26.624 0-46.976-20.352-46.976-46.933333V333.013333h-225.450666c-26.624 0-46.933333-20.352-46.933334-46.933333 0-26.666667 20.309333-47.018667 46.933334-47.018667H891.733333c26.624 0 46.976 20.352 46.976 46.976v272.384c0 25.045333-21.930667 46.976-46.933333 46.976z"
                                                fill="#172B4D" p-id="17659"></path>
                                            <path
                                                d="M115.2 763.562667c-12.501333 0-23.466667-4.693333-32.853333-14.08-18.773333-18.773333-18.773333-48.554667 0-65.749334l283.349333-283.392c18.773333-18.773333 48.554667-18.773333 65.749333 0l137.770667 137.813334 266.112-264.576c18.773333-18.773333 48.554667-18.773333 65.749333 0 18.773333 18.773333 18.773333 48.512 0 65.706666l-297.386666 299.008c-18.816 18.773333-48.554667 18.773333-65.792 0l-137.770667-137.728-250.453333 250.453334a49.493333 49.493333 0 0 1-34.432 12.544z"
                                                fill="#172B4D" p-id="17660"></path>
                                        </svg>&nbsp;Trend Line</span>
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
                                    <span class="sq_collapse_text"><svg version="1.1" id="图层_1"
                                            xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
                                            x="0" y="0" width="20" height="20" viewBox="0 0 57.35 57.72"
                                            style="enable-background:new 0 0 57.35 57.72;" xml:space="preserve">
                                            <path class="st0"
                                                d="M6.52,4.53C4.43,30.32,18.06,49.7,29.71,49.46c11.73-0.24,25.05-20.48,22.15-46.38"
                                                fill="none" stroke="black" stroke-width="5" />
                                            <path class="st0" d="M55.04,49.43c0,0,0,0-48.74,0.03" fill="none" stroke="black"
                                                stroke-width="5" />
                                        </svg>
                                        Overall Indicator</span>
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
                                    <span class="sq_collapse_text"><svg version="1.1" id="图层_1"
                                            xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
                                            x="0px" y="0px" viewBox="0 0 57.35 57.72" width="20" height="20"
                                            style="enable-background:new 0 0 57.35 57.72;" xml:space="preserve">
                                            <path class="st0"
                                                d="M6.52,4.53C4.43,30.32,18.06,49.7,29.71,49.46c11.73-0.24,25.05-20.48,22.15-46.38"
                                                fill="none" stroke="black" stroke-width="5" />
                                            <path class="st0" d="M30.64,3.08c0,0,0,0,0.04,52.84" fill="none" stroke="black"
                                                stroke-width="5" />
                                        </svg>
                                        Special Time-point</span>
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
import multiBarPanel from "./utils/multiBarPanel.vue";
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
                'Single bar chart': 'singleBarPanel',
                'Single line chart': 'singleLinePanel',
                'Multiple bar chart': 'multipleBarPanel',
                'Multiple line chart': 'multipleLinePanel'
            },
            chartTypeMap: ['Single bar chart', 'Single line chart', 'Multiple bar chart', 'Multiple line chart'],
            // tabs: {
            //     'Single bar chart': 'singleBarPanel'
            // },
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
            let selObj = dataStore.selectObject;
            if (selObj != '') {
                if (selObj == -1) {
                    this.overlayTag = [0, 0, 0, 0, 0, 0, 0, 0, 0];
                } else {
                this.overlaySetting = dataStore.state_map['state0']['overlay_setting'][selObj];

                this.overlayTag = dataStore.state_map['state0']['overlay_setting'][selObj]['overlay_tag'];}
            }
            // }
        })
    },
    components: {
        'color-picker': ColorPicker,
        'singleBarPanel': singleBarPanel,
        'multipleBarPanel': multiBarPanel
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
                let selObj = dataStore.selectObject;
                dataStore.state_map['state0']['overlay_setting'][selObj] = newVal;
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
                let selObj = dataStore.selectObject;
                // console.log(dataStore.state_map['state0'])
                if (selObj != -1 && selObj != '')
                dataStore.state_map['state0']['overlay_setting'][selObj]['overlay_tag'] = newVal;
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
    background-color: #F8F8F8;
}

.sq_collapse_title {
    width: 100%;
    text-align: start;
    display: flex;
    align-items: center;
    justify-content: space-between;
    background-color: #F8F8F8;
    /* display: flex;
    align-items: center; */
}

.sq_collapse_text {
    font-weight: bold;
    display: flex;
    align-items: center;
    justify-content: space-between;

}

.sq_collapse_content {
    /* padding: 10px 0px 10px 0px; */
    background-color: white;
    padding-left: 25px;
}
</style>
