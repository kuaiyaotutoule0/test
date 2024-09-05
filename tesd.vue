<template>
  <div class="treeWrapper">
    <div class="leftView">
      <el-input placeholder="请输入内容" v-if="relationTree.length" v-model="filterTreeName" @change="filterChange"/>
      <el-checkbox v-if="relationTree.length" class="select-box" v-model="menuNodeAll"
                   @change="handleCheckedTreeNodeAll($event)">全选
      </el-checkbox>
      <el-tree :data="relationTree" show-checkbox node-key="id" ref="tree" :props="defaultProps" @check="hanldTreeCheck"
               default-expand-all :filter-node-method="filterNode" :default-checked-keys="checkedKeys">
      </el-tree>
    </div>
    <div class="rightView">
      <header>
        <span>已选择 {{ checkList.length }} 个</span>
        <span @click="removeRightTreeAll">全部清除</span>
      </header>
      <div class="checkedItem" v-if="checkList.length">
        <li v-for="(m, i) in checkList" :class="['align-center','justify-between',m.checkFlag ? 'mark':'']" :key="i">
          <p>{{ m.name }}</p>
          <svg-icon icon-class="deleteTreeItem" @click="tagClose(m, i)"/>
        </li>
      </div>
      <div class="right-nodata f_c_m" v-else>暂无数据</div>
    </div>
  </div>
</template>
<script>
export default {
  name: "baseTree",
  props: {
    relationTree: {
      type: Array,
      default: () => [],
    },
    checkedKeys: {
      type: Array,
      default: () => [],
    },
  },
  data() {
    return {
      filterTreeName: "",
      menuNodeAll: false,
      defaultProps: {
        children: "relationResps",
        label: "name",
      },
      // 选中机器人
      checkList: [],
      checkDataList: [],
    };
  },
  mounted() {},
 
  methods: {
    filterNode(value, data) {
      if (!value) {
        return true;
      }
      return data.name.includes(value);
    },
    // 过滤
    filterChange() {
      this.$refs.tree.filter(this.filterTreeName);
    },
    // 全部清除
    removeRightTreeAll() {
      this.checkList = [];
      if (this.menuNodeAll) {
        this.menuNodeAll = !this.menuNodeAll;
      }
      const parentCheckedLength = this.$refs.tree.getCheckedKeys().length;
      if (parentCheckedLength !== 0) {
        this.$refs.tree.setCheckedNodes([]);
      }
      this.checkDataList = [];
      this.$emit("treeclick", this.checkDataList);
    },
    // 全选
    handleCheckedTreeNodeAll(data) {
      if (this.menuNodeAll) {
        //如果是当前值是全选，依次遍历节点设置勾选，同时过滤的disabled为true的
        // 深度遍历
        let stack = [...this.relationTree],
          node;
        while ((node = stack.shift())) {
          console.log(node.id);
          this.$refs.tree.setChecked(node.id, true, true);
          // 如果有子元素的话进行压栈操作
          if (node.children) stack.unshift(...node.children);
          this.checkList = this.$refs.tree.getCheckedNodes(true, false);
          this.hanldTreeCheck(this.$refs.tree.getCheckedNodes(this.checkList));
        }
      } else {
        //当前值不是全选，设置勾选列表为空
        this.$refs.tree.setCheckedKeys([]);
        this.checkList = [];
        this.$emit("treeclick", this.checkList);
      }
    },
    // 当tree 复选框被点击的时候触发
    hanldTreeCheck(data) {
      const childNodeList = this.$refs.tree.getCheckedNodes(true, false);
      this.checkList = childNodeList;
      this.checkDataList =
        (childNodeList.length &&
          childNodeList.map((instance) => {
            // 机器人
            const {
              id: equipmentId,
              name: equipmentName,
              parentId: instanceParentId,
              checkFlag: checkFlag,
            } = instance;
            // 门店
            const {
              id: storeId,
              name: storeName,
              parentId: instanceStoreParentId,
            } = this.$refs.tree.getNode(instanceParentId).data;
            // 公司
            const {id: companyId, name: companyName} =
              this.$refs.tree.getNode(instanceStoreParentId).data;
            return {
              storeId,
              storeName,
              equipmentId,
              equipmentName,
              companyId,
              companyName,
              checkFlag,
            };
          })) ||
        [];
      this.$emit("treeclick", this.checkDataList);
    },
 
    // 右侧组件点击“关闭”按钮触发
    tagClose(item, index) {
      // 在已选中项的下标中删除
      this.checkList.splice(index, 1);
      if (this.checkDataList.length) {
        this.checkDataList.splice(index, 1);
        this.$emit("treeclick", this.checkDataList);
      }
      // 在tree树控件中更改选中状态.
      //setChecked  接收三个参数，1. 勾选节点的 key 或者 data 2. boolean 类型，节点是否选中 3. boolean 类型，是否设置子节点 ，默认为 false
      this.$refs.tree.setChecked(item.id, false, true);
      // 重新计算已选中树形节点
      this.hanldTreeCheck();
    },
  },
};
</script>
<style lang="scss" scoped>
.treeWrapper {
  overflow: hidden;
  display: grid;
  grid-template-columns: 50% 50%;
  grid-auto-rows: 336px;
  margin: 10px auto;
  width: 100%;
  /* height: 336px; */
  border-radius: 6px;
  border: 1px solid #dbdbdb;
 
  .leftView {
    display: flex;
    flex-direction: column;
    /* width: 100%; */
    .el-tree {
      height: 100%;
    }
 
    .select-box {
      display: flex;
      justify-content: space-between;
      flex-direction: row-reverse;
      margin-top: 10px;
      padding: 0 18px 0 10px;
 
      .el-checkbox__label {
        font-size: 10px;
        font-weight: bold;
        color: #222222;
      }
    }
 
    .el-input {
      margin: 10px auto 0;
      width: 85% !important;
    }
 
    .el-tree {
      border: none !important;
      /* height: 100%; */
      overflow: overlay;
 
      .el-tree-node__content {
        padding-right: 10px !important;
 
        .el-checkbox {
          order: 2;
          flex: 1;
          text-align: right;
        }
 
        .custom-tree-node {
          order: 1;
 
          > span {
            display: block;
            max-width: 120px;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
          }
        }
      }
 
      > .el-tree-node > .el-tree-node__content {
        padding-left: 10px !important;
      }
    }
  }
 
  .rightView {
    /* flex-basis: 50%; */
    position: relative;
    display: flex;
    flex-direction: column;
    padding: 0 0 0 18px;
    /* width: 100%; */
    border-left: 1px solid #dbdbdb;
 
    > header {
      display: flex;
      justify-content: space-between;
      margin: 16px 0 12px 0;
      padding-right: 10px;
      font-size: 10px;
 
      > span:nth-child(1) {
        color: #222222;
      }
 
      > span:nth-child(2) {
        color: #592c82;
        cursor: pointer;
      }
    }
 
    .checkedItem {
      height: 100%;
      overflow: overlay;
 
      > li {
        height: 26px;
        margin-right: 18px;
      }
 
      .mark {
        color: red;
      }
    }
  }
 
  .right-nodata {
    color: #909399;
    position: absolute;
    left: 50%;
    top: 60%;
    transform: translate(-50%, -50%);
  }
}
</style>
