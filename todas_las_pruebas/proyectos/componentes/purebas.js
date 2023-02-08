class Node1 {
    constructor (value) {
        this.left= null;
        this.right= null;
        this.value=value;
    }
}
class BinarySearchtree {
    constructor(){
        this.root=null;
    }
    insert(value){
         const newNode = new Node1(value);
         if (this.root === null){
            this.root = newNode;
         }
         else {
            let currentNode=this.root;
            while (true){
                if (value< currentNode.value){
                    if (!currentNode.left){
                        currentNode.left=newNode;
                        return this;
                    }
                    currentNode= currentNode.left
                } else {
                    if(!currentNode.right){
                        currentNode.right=newNode;
                        return this;
                    }
                    currentNode=currentNode.right;
                }
            }         
        }
    }
    search(value) {
        let currentNode=this.root;
        while (true){
            if(value===currentNode.value){
                console.log(currentNode);
                return this;
            }else{
                if(value<currentNode.value){
                    currentNode=currentNode.left;
                    if(value===currentNode.value){
                        console.log(currentNode);
                        return this;
                    }
                }
                else{
                    currentNode=currentNode.right;
                    if(value===currentNode.value){
                        console.log(currentNode);
                        return this;
                    }
                }
            }
        }
    }
}

const tree= new BinarySearchtree();
tree.insert(10);
tree.insert(4);
tree.insert(20);
tree.insert(2);
tree.insert(8);
tree.insert(17);
tree.insert(170);
tree.search(4);
