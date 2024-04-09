import random

def find_available_groups(patient_data, max_group_size, group_range):
    # Filter out groups that have already exceeded the max_group_size.
    return [str(group) for group in group_range if patient_data[patient_data['Group'] == str(group)].shape[0] < max_group_size]

def assign_group(patient_data, factor, available_groups):
    factor_data = patient_data[patient_data['Factor'] == factor]
    group_counts = factor_data['Group'].value_counts()

    # Assign the factor to any group if it's the first assignment for this factor,
    # or if the factor is evenly assigned across the all groups.
    non_nan_count = factor_data.iloc[:, 2].notna().sum()    #Calculate the number of non-NaN values in the third column of factor_data
    if len(factor_data) == 1 or (non_nan_count) / len(available_groups) == 0:
        return random.choice(available_groups)

    # If the factor is currently assigned only to a subset of groups,
    # we need to only assign the factor to unassigned groups.
    if len(group_counts) < len(available_groups):
        unassigned_groups = [group for group in available_groups if group not in group_counts]
        return random.choice(unassigned_groups)

    # If the factor is neither in both of the above two cases,
    # randomly assign it to one of the groups with the least number of assignments.
    # but only among the available groups.
    min_count = group_counts.reindex(available_groups).min()    # The minimum of assigned number
    min_count_groups = [group for group in available_groups if group_counts.get(group, 0) == min_count]
    return random.choice(min_count_groups)


def dynamic_stratified_randomization(patient_data, factor, max_group_size, group_len):
    available_groups = find_available_groups(patient_data, max_group_size, range(1, group_len + 1))
    assigned_group = assign_group(patient_data, factor, available_groups)

    return assigned_group


