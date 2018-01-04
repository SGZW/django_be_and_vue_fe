<template>
    <div class="foot-room">
        <div class="powered-by">
            <Poptip trigger="hover" content="Powered-By ZhangWei">
                <Icon type="ios-monitor" size="32" class="foot-icon"></Icon>
            </Poptip>
        </div>
    </div>
</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    .foot-room{
        width: 100%;
        height: 50px;
        border-top: 1px solid #EAECEF;
        padding: 10px;
        font-size: 15px;
    }
    .powered-by{
        font-size: 13px;
        line-height: 13px;
    }
    .foot-icon{
        color: #959DA5;
    }
    .foot-icon:hover{
        color: #3399ff;
    }
</style>

<script>
    export default {
        name: 'foot-room',
        data: () => {
            return {};
        },
    };
</script>
