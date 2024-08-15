<template>
  <div class="container">  
    <el-row>  
      <el-col :span="12">  
        <el-tree  
          :data="data"  
          :props="props"  
          show-checkbox  
          node-key="id"  
          @check-change="handleCheckChange"  
          :render-content="renderContent"
        ></el-tree>  
      </el-col>  
      <el-col :span="12">  
        <ul>  
          <li v-for="leaf in selectedLeafValues" :key="leaf.id">{{ leaf.label }}</li>  
        </ul>  
      </el-col>  
    </el-row>  
  </div>  
</template>

<script>
export default {
  data() {
    return {
      
      data: [],
      selectedLeafValues: [],// 存储当前所有选中的叶子节点的值,
      props: {
        label: 'label',
        children: 'children',
      }
    }
  },
  created() {
    const te = {
          "3.0": {
            "200": {
              "A20": {},
              "B20": {}
            },
            "210": {
              "C20": {},
              "D20": {}
            }
          },
          "2.0": {
            "300": {
              "A30": {},
              "B40": {}
            },
            "410": {
              "C50": {},
              "D60": {}
            }
          },
          "1.0": {
            "500": {
              "E70": {},
              "F80": {}
            },
            "610": {
              "G50": {},
              "H90": {}
            }
          }
        }
        this.data = this.convertDataToTree(te)
  },
  methods: {
    handleCheckChange(data, checked, indeterminate) {  
      // 这里需要遍历整个树，找到所有叶子节点，并更新selectedLeafValues  
      // 但为了简化，这里只更新当前节点的状态（假设你希望即点即选）  
      // if (checked && this.isLeaf(data)) {  
      //   this.selectedLeafValues.push({ ...data, checked });  
      // } else if (!checked && this.selectedLeafValues.some(item => item.id === data.id)) {  
      //   this.selectedLeafValues = this.selectedLeafValues.filter(item => item.id !== data.id);  
      // }  
      console.log(data)
      console.log(checked)
      console.log(indeterminate)
      if (checked && this.isLeaf(data)) {
        this.selectedLeafValues.push({ ...data, checked })
      } else if (!checked && this.isLeaf(data)) {
        const index = this.selectedLeafValues.findIndex(item => item.id === data.id);  
  
        // 如果找到了（索引不是-1），则删除它  
        if (index !== -1) {  
          this.selectedLeafValues.splice(index, 1);  
        }
      }
      // 注意：上面的逻辑很基础，没有处理所有情况（如取消勾选父节点时自动取消勾选子节点）  
      // 你可能需要一个更复杂的函数来遍历整个树并更新selectedLeafValues  
    },  
    isLeaf(node) {  
      // 判断节点是否为叶子节点  
      return !node.children || node.children.length === 0;  
    },
    recurse(obj, path = '') {
        let treeNodes = []
        for (let key in obj) {
          // 构建当前节点的 label，这里简单地将路径和当前 key 连接起来  
          let label = `${path ? path + '-' : ''}${key}`
          let node = { label }
          // 如果当前对象的值是对象，则递归处理  
          if (typeof obj[key] === 'object' && obj[key] !== null) {
            node.children = this.recurse(obj[key], label)
          }
          // 将节点添加到结果数组中  
          treeNodes.push(node)
        }
        return treeNodes
      },
    convertDataToTree(data) {
      // 定义一个函数来递归处理对象  
      // 调用递归函数并返回结果  
      return this.recurse(data);
    },
    // 自定义渲染函数  
    renderContent(h, { node, data, store }) {  
      // 假设我们只想要显示 label 的前4个字符  
      const subLabel = data.label.split('-')
      return h('span', subLabel[subLabel.length-1])  
    }  
  }
}
</script>
