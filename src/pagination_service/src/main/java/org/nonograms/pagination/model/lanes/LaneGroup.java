package org.nonograms.pagination.model.lanes;

import java.util.LinkedList;
import java.util.List;
import java.util.stream.Stream;

/**
 * Group of {@link org.nonograms.pagination.model.lanes.Lane} objects.
 */
public final class LaneGroup extends LaneNode {

    private final List<LaneNode> children;
    /**
     * Size of the underlying groups for the current level. It can take a
     *     special value of {@link #INDIVIDUAL_LANES} if no underlying
     *     groups are expected.
     **/
    private final int currentLevelSize;
    /**
     * The index (in {@link #LEVEL_SIZES}) of the level size for underlying
     *     groups.
     **/
    private final Integer underlyingLevelIndex;

    /**
     * The sizes of lane group levels (e.g. the value of [5, 10] means that
     *     the entire lanes set is grouped by 10, every subgroup is of size 5,
     *     and it has no further subgroups, thus contains individual lanes)
     */
    private static final List<Integer> LEVEL_SIZES = List.of(5, 10);
    /**
     * The highest (rightmost) index in {@link #LEVEL_SIZES}
     */
    private static final int TOP_LEVEL = LEVEL_SIZES.size() - 1;
    /**
     * Special underlying index value when no further levels are expected
     */
    private static final int LEVEL_NONE = -1;
    /**
     * Special level size to indicate no grouping
     */
    private static final int INDIVIDUAL_LANES = 1;

    /**
     * See {@link #getActualSize()}.
     */
    private int actualSize;

    public LaneGroup() {
        this(TOP_LEVEL);
    }

    private LaneGroup(int level) {
        this.children = new LinkedList<>();

        this.currentLevelSize = level == LEVEL_NONE ? INDIVIDUAL_LANES : LEVEL_SIZES.get(level);
        this.underlyingLevelIndex = level == LEVEL_NONE ? null : level - 1;

        this.actualSize = 0;
    }

    /**
     * Adds the provided lane to one of the underlying groups (or
     *     directly to this group if no underlying ones are
     *     expected)
     * @param lane The lane to add
     */
    private void addLane(Lane lane) {
        if (currentLevelSize == INDIVIDUAL_LANES) {
            children.add(lane);
        } else { // We're on a level with underlying groups
            // If there were no underlying groups or the current one is full, we create a new one
            if (children.isEmpty() || children.getLast().getActualSize() == currentLevelSize) {
                children.add(new LaneGroup(underlyingLevelIndex));
            }

            LaneGroup currentUnderlyingGroup = (LaneGroup) children.getLast();
            currentUnderlyingGroup.addLane(lane);
        }

        actualSize++;
    }

    /**
     * Populates the group with the provided list of clues (one per lane).
     * @param clueLists     List of clues (which are lists of integer values) for the lanes to add
     */
    public void populate(final List<List<Integer>> clueLists) {
        clueLists.forEach(clueList -> addLane(new Lane(clueList)));
    }

    /**
     * The total size of all the underlying groups (or the count of individual
     *     lanes if no underlying groups are expected)
     */
    @Override
    protected int getActualSize() {
        return actualSize;
    }

    public Stream<LaneNode> getChildrenStream() {
        return children.stream();
    }
}

