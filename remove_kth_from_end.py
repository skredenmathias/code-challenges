def remove_kth_from_end(head, k):
    # traverse through LL
    current = head
    cache = {}
    count = 0
    while current is not None:
        # store each node/node.value as cache[node] = index
        cache[count] = current
        if current.next == None and (k <= count + 1) and k > 0:
            # find node to delete
            node_to_delete = cache[count - k + 1]
            # Set node pointer to None
            # node_to_delete.next = None
            # Find previous node
            previous_node = cache[count - k]

            # If node_to_delete is not the tail
            if (count - k + 2) in cache:
                print('there')
                # Find next node
                next_node = cache[count - k + 2]
            # Set previous pointer to next
                previous_node.next = next_node
                return head
            else:
                print('here')
                # If node_to_delete is the tail
                previous_node.next = None
                return head
        count += 1
        current = current.next
    print('over here')
    return head

    # When we reach the end of LL:
        # removed_node = k - last index, unless k > last index
            # To remove:
                # set removed_node - 1.next to removed_node + 1
                # maybe set removed_node.next to None