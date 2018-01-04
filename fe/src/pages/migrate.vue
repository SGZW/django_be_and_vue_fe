<template>
    <Card>
        <p slot="title">
             户籍/人员 迁出信息查询
        </p>
        <Form inline>
            <FormItem label="户籍号">
                <Input v-model="search_form.household_num" type="text" placeholder="请填入户籍号"></Input>
            </FormItem>
            <FormItem label="身份证号">
                <Input v-model="search_form.id_card" type="text" placeholder="请填入身份证号"></Input>
            </FormItem>
            <FormItem label="性别">
                <Select v-model="search_form.sex" placeholder="请选择性别" style="width: 150px;">
                    <Option v-for="i in sex_type" :value="i.value" :key="i.value">{{ i.label }}</Option>
                </Select>
            </FormItem>
            <FormItem label="民族">
                <Input v-model="search_form.nation" type="text" placeholder="请选择民族"></Input>
            </FormItem>
            <FormItem label="姓名">
                <Input v-model="search_form.name" type="text" placeholder="请选择姓名"></Input>
            </FormItem>
        </Form>
        <Form inline>
            <FormItem>
                <Button type="primary" @click="search">查询</Button>
            </FormItem>
        </Form>
        <Table stripe border :columns="data_table.column" :data="data_table.data"></Table>
    </Card>
</template>

<script>
    import request from '@/libs/request';
    export default {
        data () {
            return {
                name: 'migrate',
                search_form: {
                    household_num: '',
                    id_card: '',
                    sex: '',
                    nation: '',
                    name: '',
                },
                sex_type: [
                    {
                        label: '男',
                        value: '男',
                    },
                    {
                        label: '女',
                        value: '女',
                    },
                ],
                relation_type: [
                    {
                        label: '户主',
                        value: '户主',
                    },
                    {
                        label: '非户主',
                        value: '非户主',
                    },
                ],
                data_table: {
                    column: [
                        {
                            title: '身份证号',
                            key: 'id',
                            width: 180,
                            ellipsis: true,
                        },
                        {
                            title: '户号',
                            key: 'household_num',
                        },
                        {
                            title: '姓名',
                            key: 'name',
                        },
                        {
                            title: '性别',
                            key: 'sex',
                        },
                        {
                            title: '户主关系',
                            key: 'relation',
                        },
                        {
                            title: '民族',
                            key: 'nation',
                        },
                        {
                            title: '地址',
                            key: 'address',
                        },
                        {
                            title: '迁往何地',
                            key: 'where_out',
                        },
                        {
                            title: '迁出时间',
                            key: 'date_out',
                            width: 120,
                        },
                    ],
                    data: [],
                },
            };
        },
        methods: {
            search () {
                request({
                    url: '/api/get_search_data/',
                    method: 'get',
                    params: {
                        household_num: this.search_form.household_num,
                        id: this.search_form.id_card,
                        sex: this.search_form.sex,
                        nation: this.search_form.nation,
                        name: this.search_form.name,
                        is_out: 1,
                    },
                }).then((res) => {
                    this.data_table.data = res.search_data;
                });
            },
            refresh () {
                request({
                    url: '/api/get_init_data/',
                    method: 'get',
                    params: {
                        is_out: 1,
                    },
                }).then((res) => {
                    this.data_table.data = res.init_data;
                });
            },
        },
        mounted () {
            this.refresh();
        },
    };
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
