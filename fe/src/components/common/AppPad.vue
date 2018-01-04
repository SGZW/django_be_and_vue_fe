<template>
    <Menu-item name="app-pad">
        <Poptip title="其它平台" placement="bottom-end">
            <Badge>
                <Icon type="ios-keypad" size="26"></Icon>
            </Badge>
            <div class="app-list" slot="content">
            </div>
        </Poptip>
    </Menu-item>
</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    .app-list {
        width: 150px;
        height: 300px;
        overflow-y: auto;
    }
</style>

<script>
    import { mapState } from 'vuex';

    export default {
        name: 'app-pad',
        data: () => {
            return {};
        },
        computed: mapState([
            'common',
        ]),
    };
</script>
