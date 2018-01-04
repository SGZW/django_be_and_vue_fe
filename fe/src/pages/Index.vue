<template>
    <Card>
        <p slot="title">
             户籍/人员 迁入管理
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
            <FormItem>
                <Button type="primary" @click="add">户籍/人员  迁入</Button>
            </FormItem>
        </Form>
        <Table stripe border :columns="data_table.column" :data="data_table.data"></Table>
        <Modal v-model="add_form.seen" :title="add_form.title" width="800" :styles="{top: '40px'}" @on-ok="insert" okText="新增">
                <Form>
                    <FormItem label="户号" >
                        <Input v-model="add_form.household_num"  type="text"></Input>
                    </FormItem>
                    <FormItem label="身份证" >
                        <Input v-model="add_form.id_card" type="text"></Input>
                    </FormItem>
                    <FormItem label="性别">
                        <Select v-model="add_form.sex" placeholder="请选择性别" style="width: 150px;">
                            <Option v-for="i in sex_type" :value="i.value" :key="i.value">{{ i.label }}</Option>
                        </Select>
                    </FormItem>
                    <FormItem label="民族" >
                        <Input v-model="add_form.nation" type="text"></Input>
                    </FormItem>
                    <FormItem label="姓名" >
                        <Input v-model="add_form.name"  type="text"></Input>
                    </FormItem>
                    <FormItem label="户主关系">
                        <Select v-model="add_form.relation" style="width: 150px;"placeholder="请选择户主关系" >
                            <Option v-for="i in relation_type" :value="i.value" :key="i.value">{{ i.label }}</Option>
                        </Select>
                    </FormItem>
                    <FormItem label="地址">
                        <Input v-model="add_form.address"  type="text"></Input>
                    </FormItem>
                    <FormItem label="何地迁入" >
                        <Input v-model="add_form.where_in"  type="text"></Input>
                    </FormItem>
                    <FormItem label="迁入时间" >
                        <DatePicker type="date"  placeholder="请选择日期" style="width: 200px" @on-change="handleChange_in"></DatePicker>
                    </FormItem>
                </Form>
        </Modal>
        <Modal v-model="detail_form.seen" :title="detail_form.title" width="800" :styles="{top: '40px'}" @on-ok="migrate" okText="迁出">
                <Alert type="error">
                    ⚠️:迁出户主将迁出整户人员
                </Alert>
                <Form>
                    <FormItem label="户号" >
                        <Input v-model="detail_form.household_num"  disabled type="text"></Input>
                    </FormItem>
                    <FormItem label="身份证" >
                        <Input v-model="detail_form.id" disabled type="text"></Input>
                    </FormItem>
                    <FormItem label="姓名" >
                        <Input v-model="detail_form.name"  disabled type="text"></Input>
                    </FormItem>
                    <FormItem label="户主关系">
                        <Input v-model="detail_form.relation"  disabled type="text"></Input>
                    </FormItem>
                    <FormItem label="迁往何地" >
                        <Input v-model="detail_form.where_out"  type="text"></Input>
                    </FormItem>
                    <FormItem label="迁出时间" >
                        <DatePicker type="date"  placeholder="请选择日期" style="width: 200px" @on-change="handleChange_out"></DatePicker>
                    </FormItem>
                </Form>
        </Modal>
    </Card>
</template>

<script>
    import request from '@/libs/request';
    export default {
        data () {
            return {
                name: 'index',
                detail_form: {
                    seen: false,
                    title: '详细信息',
                    household_num: '',
                    relation: '',
                    id: '',
                    name: '',
                    where_out: '',
                    date_out: '',
                },
                add_form: {
                    seen: false,
                    title: '户籍/人员 迁入管理',
                    household_num: '',
                    id_card: '',
                    sex: '',
                    nation: '',
                    name: '',
                    relation: '',
                    address: '',
                    where_in: '',
                    date_in: '',
                },
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
                            title: '何地迁入',
                            key: 'where_in',
                        },
                        {
                            title: '迁入时间',
                            key: 'date_in',
                            width: 120,
                        },
                        {
                            title: 'Action',
                            key: 'action',
                            width: 100,
                            align: 'center',
                            render: (h, params) => {
                                return h('div', [
                                    h('Button', {
                                        props: {
                                            type: 'primary',
                                            size: 'small',
                                        },
                                        style: {
                                            marginRight: '5px',
                                        },
                                        on: {
                                            click: () => {
                                                this.show(params.index);
                                            },
                                        },
                                    }, '详情'),
                                ]);
                            },
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
                        is_out: 0,
                    },
                }).then((res) => {
                    this.data_table.data = res.search_data;
                });
            },
            add () {
                this.add_form.seen = true;
            },
            check () {
                if (this.add_form.household_num.trim() === '') {
                    this.$Message.info('户籍号为空');
                    return false;
                }
                if (this.add_form.id_card.trim() === '') {
                    this.$Message.info('身份证号为空');
                    return false;
                }
                if (this.add_form.sex.trim() === '') {
                    this.$Message.info('性别为空');
                    return false;
                }
                if (this.add_form.nation.trim() === '') {
                    this.$Message.info('民族为空');
                    return false;
                }
                if (this.add_form.name.trim() === '') {
                    this.$Message.info('姓名为空');
                    return false;
                }
                if (this.add_form.relation.trim() === '') {
                    this.$Message.info('户主关系为空');
                    return false;
                }
                if (this.add_form.address.trim() === '') {
                    this.$Message.info('地址为空');
                    return false;
                }
                if (this.add_form.where_in.trim() === '') {
                    this.$Message.info('何地迁入为空');
                    return false;
                }
                if (this.add_form.date_in.trim() === '') {
                    this.$Message.info('何时迁入为空');
                    return false;
                }
                return true;
            },
            insert () {
                if (!this.check()) {
                    return;
                }
                request({
                    url: '/api/add_insert_data/',
                    method: 'get',
                    params: {
                        household_num: this.add_form.household_num.trim(),
                        id: this.add_form.id_card.trim(),
                        sex: this.add_form.sex.trim(),
                        nation: this.add_form.nation.trim(),
                        name: this.add_form.name.trim(),
                        relation: this.add_form.relation.trim(),
                        address: this.add_form.address.trim(),
                        where_in: this.add_form.where_in.trim(),
                        date_in: this.add_form.date_in.trim(),
                    },
                }).then((res) => {
                    this.$Message.info(res.status);
                    this.refresh();
                });
            },
            handleChange_in (date) {
                this.add_form.date_in = date;
            },
            handleChange_out (date) {
                this.detail_form.date_out = date;
            },
            refresh () {
                request({
                    url: '/api/get_init_data/',
                    method: 'get',
                    params: {
                        is_out: 0,
                    },
                }).then((res) => {
                    this.data_table.data = res.init_data;
                });
            },
            show (index) {
                this.detail_form.id = this.data_table.data[index].id;
                this.detail_form.household_num = this.data_table.data[index].household_num;
                this.detail_form.relation = this.data_table.data[index].relation;
                this.detail_form.name = this.data_table.data[index].name;
                this.detail_form.seen = true;
            },
            migrate () {
                if (this.detail_form.where_out.trim() === '') {
                    this.$Message.info('迁出地为空');
                    return;
                }
                if (this.detail_form.date_out.trim() === '') {
                    this.$Message.info('迁出日期为空');
                    return;
                }
                request({
                    url: '/api/migrate/',
                    method: 'get',
                    params: {
                        id: this.detail_form.id.trim(),
                        household_num: this.detail_form.household_num.trim(),
                        relation: this.detail_form.relation.trim(),
                        where_out: this.detail_form.where_out.trim(),
                        date_out: this.detail_form.date_out.trim(),
                    },
                }).then((res) => {
                    this.$Message.info(res.status);
                    this.refresh();
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
